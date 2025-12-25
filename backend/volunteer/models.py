from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        abstract = True


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_volunteer = models.BooleanField("Волонтёр", default=False)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    city = models.CharField("Город", max_length=100, blank=True)

    def __str__(self):
        return f"Профиль {self.user.username}"


class Event(TimeStampedModel):
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    date_start = models.DateTimeField("Начало")
    date_end = models.DateTimeField("Окончание")
    location = models.CharField("Место", max_length=300)
    organizer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="organized_events",
        verbose_name="Организатор"
    )
    max_participants = models.PositiveIntegerField("Макс. участников", default=50)
    is_active = models.BooleanField("Активно", default=True)

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ["-date_start"]

    def __str__(self):
        return self.title

    @property
    def current_participants_count(self):
        return self.participations.filter(status="approved").count()


class Participation(TimeStampedModel):
    STATUS_CHOICES = (
        ("pending", "На рассмотрении"),
        ("approved", "Одобрено"),
        ("rejected", "Отклонено"),
        ("canceled", "Отменено"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="participations",
        verbose_name="Волонтёр"
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="participations",
        verbose_name="Мероприятие"
    )
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default="pending")
    comment = models.TextField("Комментарий волонтёра", blank=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        unique_together = ["user", "event"]

    def __str__(self):
        return f"{self.user} → {self.event}"