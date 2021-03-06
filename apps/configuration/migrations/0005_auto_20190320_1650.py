# Generated by Django 2.1.5 on 2019-03-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0004_auto_20190320_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rate',
            options={'ordering': ['detail'], 'verbose_name': 'Tabla de tarifa', 'verbose_name_plural': 'Tabla de Tarifas'},
        ),
        migrations.AlterModelOptions(
            name='typesservice',
            options={'ordering': ['detail'], 'verbose_name': 'Tipo de servicio', 'verbose_name_plural': 'Tipo de servicios'},
        ),
        migrations.AlterField(
            model_name='rate',
            name='exceeding_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Valor por excedente'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='lowre_range',
            field=models.IntegerField(default=11, verbose_name='Rango Inicial'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='top_range',
            field=models.IntegerField(default=11, verbose_name='Rango Superior'),
        ),
    ]
