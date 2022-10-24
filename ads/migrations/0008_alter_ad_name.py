# Generated by Django 4.1.1 on 2022-10-21 07:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_category_slug_alter_ad_is_published_alter_ad_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]