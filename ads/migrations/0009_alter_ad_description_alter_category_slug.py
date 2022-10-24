# Generated by Django 4.1.1 on 2022-10-23 04:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_alter_ad_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]