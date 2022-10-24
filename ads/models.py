from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(unique=True, max_length=10, null=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=500, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='ads')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='ads')

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='selections')
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
