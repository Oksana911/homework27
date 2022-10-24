from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date


USER_MIN_AGE = 9


def check_birth_date(value):
    diff = relativedelta(date.today(), value)
    if diff.years < USER_MIN_AGE:
        raise ValidationError("User's age should be more then 9")


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLES = [
        ('member', 'user'),
        ('admin', 'admin'),
        ('moderator', 'moderator'),
    ]

    role = models.CharField(max_length=10, choices=ROLES, default='user')
    age = models.IntegerField(null=True, blank=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(null=True, validators=[check_birth_date])
    email = models.EmailField(null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Пользователь {self.username}"
