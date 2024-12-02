from django.contrib.auth.models import AbstractUser

from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    name = models.CharField(
        max_length=10,
        verbose_name="Имя пользователя",
        **NULLABLE
    )
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(
        max_length=25,
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Укажите номер"
    )
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="Аватар",
        **NULLABLE
    )
    tg_chat_id = models.CharField(
        max_length=100,
        verbose_name='телеграмм chat_id',
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
