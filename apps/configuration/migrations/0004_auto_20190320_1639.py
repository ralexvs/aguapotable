# Generated by Django 2.1.5 on 2019-03-20 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0003_auto_20190320_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=50, verbose_name='Detalle')),
                ('lowre_range', models.IntegerField(verbose_name='Rango Inicial')),
                ('top_range', models.IntegerField(default=2.25, verbose_name='Rango Superior')),
                ('exceeding_rate', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Tarifa base')),
                ('base_rate', models.BooleanField(default=False, verbose_name='Es tarifa base?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name': 'Tabla de tarifa',
                'verbose_name_plural': 'Tabla de Tarifas',
            },
        ),
        migrations.CreateModel(
            name='TypesService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=50, verbose_name='detalle')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name': 'Tipo de servicio',
                'verbose_name_plural': 'Tipo de servicios',
            },
        ),
        migrations.AddField(
            model_name='rate',
            name='types_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.TypesService', verbose_name='Tipo de servicio'),
        ),
    ]
