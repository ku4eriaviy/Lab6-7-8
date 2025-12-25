from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event, Participation, UserProfile


class UserSerializer(serializers.ModelSerializer):
    is_volunteer = serializers.BooleanField(source='profile.is_volunteer', read_only=True)
    phone = serializers.CharField(source='profile.phone', read_only=True)
    city = serializers.CharField(source='profile.city', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_volunteer', 'phone', 'city']
        read_only_fields = ['id', 'is_volunteer', 'phone', 'city']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_volunteer = serializers.BooleanField(default=False, write_only=True)
    phone = serializers.CharField(max_length=20, required=False, write_only=True)
    city = serializers.CharField(max_length=100, required=False, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'is_volunteer', 'phone', 'city']

    def create(self, validated_data):
        profile_data = {
            'is_volunteer': validated_data.pop('is_volunteer', False),
            'phone': validated_data.pop('phone', ''),
            'city': validated_data.pop('city', ''),
        }
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        UserProfile.objects.create(user=user, **profile_data)
        return user


class EventSerializer(serializers.ModelSerializer):
    organizer_name = serializers.CharField(source="organizer.get_full_name", read_only=True)
    participants_count = serializers.IntegerField(source="current_participants_count", read_only=True)

    class Meta:
        model = Event
        fields = [
            "id", "title", "description", "date_start", "date_end",
            "location", "organizer", "organizer_name", "max_participants",
            "participants_count", "is_active", "created_at", "updated_at"
        ]
        read_only_fields = ["organizer", "participants_count", "created_at", "updated_at"]


class ParticipationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.get_full_name", read_only=True)
    event_title = serializers.CharField(source="event.title", read_only=True)

    class Meta:
        model = Participation
        fields = [
            "id", "user", "user_name", "event", "event_title",
            "status", "comment", "created_at", "updated_at"
        ]
        read_only_fields = ["user", "created_at", "updated_at"]