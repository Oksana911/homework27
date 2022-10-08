from django.db import models

from users.models import User


class Category(models.Model):
    name = models.SlugField(max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):

    name = models.CharField(max_length=100)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500, null=True)
    is_published = models.BooleanField()
    image = models.ImageField(upload_to='image/')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
