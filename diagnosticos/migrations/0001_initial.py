# Generated by Django 3.2.9 on 2021-12-08 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ordenestrabajo', '0002_auto_20211202_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoría')),
                ('opcion', models.CharField(max_length=100, verbose_name='Opcion')),
                ('detalle', models.CharField(max_length=500, verbose_name='Detalles')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('orden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ordenestrabajo.ordentrabajo')),
            ],
        ),
    ]
