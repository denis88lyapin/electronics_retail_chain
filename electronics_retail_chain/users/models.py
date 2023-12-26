from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    city = models.CharField(max_length=150, verbose_name=_('City'), **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name=_('avatar'), **NULLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
