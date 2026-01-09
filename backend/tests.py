# volunteer/tests.py
from datetime import timedelta
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Event, Participation, UserProfile


class VolunteerAPITests(APITestCase):
    def setUp(self):
        # Обычный пользователь (волонтёр)
        self.volunteer = User.objects.create_user(
            username='volunteer',
            email='volunteer@example.com',
            password='testpass123'
        )
        UserProfile.objects.create(user=self.volunteer, is_volunteer=True, phone='+79991234567', city='Москва')

        # Администратор
        self.admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )

        # Событие, созданное админом
        self.event = Event.objects.create(
            title='Благотворительный забег',
            description='Помогаем детям',
            date_start=timezone.now() + timedelta(days=7),
            date_end=timezone.now() + timedelta(days=7, hours=4),
            location='Парк Горького, Москва',
            organizer=self.admin,
            max_participants=100,
            is_active=True
        )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'strongpass123',
            'first_name': 'Иван',
            'last_name': 'Петров',
            'is_volunteer': True,
            'phone': '+79998887766',
            'city': 'Санкт-Петербург'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        profile = UserProfile.objects.get(user__username='newuser')
        self.assertTrue(profile.is_volunteer)
        self.assertEqual(profile.phone, '+79998887766')
        self.assertEqual(profile.city, 'Санкт-Петербург')

    def test_get_user_profile(self):
        tokens = self.get_tokens_for_user(self.volunteer)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])
        url = reverse('user-profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'volunteer')
        self.assertTrue(response.data['is_volunteer'])
        self.assertEqual(response.data['phone'], '+79991234567')

    def test_event_list(self):
        url = reverse('event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Благотворительный забег')
        self.assertEqual(response.data['results'][0]['participants_count'], 0)


    def test_event_create_by_regular_user_forbidden(self):
        tokens = self.get_tokens_for_user(self.volunteer)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])

        url = reverse('event-list')
        data = {
            'title': 'Нельзя создать',
            'description': '...',
            'date_start': timezone.now().isoformat(),
            'date_end': (timezone.now() + timedelta(hours=2)).isoformat(),
            'location': 'Где-то'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_participate_in_event(self):
        tokens = self.get_tokens_for_user(self.volunteer)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])

        url = reverse('event-participate', kwargs={'pk': self.event.pk})
        data = {'comment': 'Хочу помочь!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Participation.objects.filter(user=self.volunteer, event=self.event).exists())
        participation = Participation.objects.get(user=self.volunteer, event=self.event)
        self.assertEqual(participation.status, 'pending')
        self.assertEqual(participation.comment, 'Хочу помочь!')

        # Проверка, что количество участников обновилось
        event_response = self.client.get(reverse('event-detail', kwargs={'pk': self.event.pk}))
        self.assertEqual(event_response.data['participants_count'], 0)  # пока pending, не считается

    def test_participate_twice_forbidden(self):
        Participation.objects.create(user=self.volunteer, event=self.event, status='pending')

        tokens = self.get_tokens_for_user(self.volunteer)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])

        url = reverse('event-participate', kwargs={'pk': self.event.pk})
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('уже подали заявку', response.data['detail'])

    def test_my_participations(self):
        Participation.objects.create(user=self.volunteer, event=self.event, status='pending', comment='Готов помочь')

        tokens = self.get_tokens_for_user(self.volunteer)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])

        url = reverse('participation-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['event_title'], self.event.title)
        self.assertEqual(response.data['results'][0]['status'], 'pending')

    def test_admin_sees_all_participations(self):
        other_user = User.objects.create_user(username='other', password='pass')
        Participation.objects.create(user=self.volunteer, event=self.event, status='pending')
        Participation.objects.create(user=other_user, event=self.event, status='approved')

        tokens = self.get_tokens_for_user(self.admin)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])

        url = reverse('participation-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)