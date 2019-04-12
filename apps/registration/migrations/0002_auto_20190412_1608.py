# Generated by Django 2.1.5 on 2019-04-12 21:08

import apps.registration.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=apps.registration.models.custom_upload_to, verbose_name='Avatar'),
        ),
    ]
