from django.db import models


class Category(models.Model):
    name = models.SlugField(max_length=50)

    # def __str__(self):
    #     return self.name


class Ads(models.Model):

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=300, null=True)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField()
