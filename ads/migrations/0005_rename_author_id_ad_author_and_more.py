# Generated by Django 4.1.1 on 2022-10-10 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_ad_author_id_alter_ad_category_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='category_id',
            new_name='category',
        ),
    ]
