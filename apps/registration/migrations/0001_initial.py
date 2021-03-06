# Generated by Django 2.1.5 on 2019-04-06 20:00

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='registration/profile', verbose_name='Avatar')),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Biografía')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
    ]
