# Generated by Django 2.1.5 on 2019-03-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_auto_20190320_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimieno'),
        ),
    ]
