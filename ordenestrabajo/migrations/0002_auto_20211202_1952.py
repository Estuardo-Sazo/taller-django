# Generated by Django 3.2.9 on 2021-12-03 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_rename_vehiculos_vehiculo'),
        ('clientes', '0001_initial'),
        ('ordenestrabajo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordentrabajo',
            name='Vehiculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo'),
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
        ),
    ]
