# Generated by Django 2.1.5 on 2019-03-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0005_auto_20190320_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='basic_rate',
            field=models.BooleanField(default=False, verbose_name='Es tarifa base?'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='base_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Tarifa base'),
        ),
    ]
