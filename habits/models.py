from django.db import models

from config import settings
from users.models import NULLABLE


class Habits(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Создатель привычки",
        **NULLABLE
    )
    when_to_perform = models.TimeField(
        verbose_name="Когда необходимо выполнить",
        help_text="Часы:Минуты:Секунды"
    )
    location = models.CharField(max_length=20, verbose_name="Место выполнения")
    act = models.CharField(
        max_length=50,
        verbose_name="Действие, которое подразумевает привычку"
    )
    pleasant_habit = models.BooleanField(
        default=True,
        help_text="Признак приятной привычки",
        verbose_name="Признак приятной привычки",
    )
    associated_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        **NULLABLE
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        verbose_name="Частота выполнения привычки (в днях)"
    )
    reward = models.CharField(
        max_length=200,
        verbose_name="Вознаграждение",
        **NULLABLE
    )
    time_to_complete = models.TimeField(
        verbose_name="Время, которое затрачивается на выполнение привычки",
        help_text="Часы:Минуты:Секунды",
    )
    is_public = models.BooleanField(
        default=True,
        help_text="Признак публичности привычки",
        verbose_name="Публичность привычки",
    )

    def __str__(self):
        return f'Я буду {self.act} в {self.when_to_perform} в {self.location}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
