from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [
        ('user', 'member'),
        ('admin', 'admin'),
        ('moderator', 'moderator'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLES, default='user')
    age = models.IntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Пользователь {self.username}"
