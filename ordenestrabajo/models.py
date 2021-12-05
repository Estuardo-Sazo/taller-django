from django.db import models
from clientes.models import Cliente
from vehiculos.models import Vehiculo
# Create your models here.
class OrdenTrabajo(models.Model):
    Nuevo='Nuevo'
    Proceso='Proceso'
    Finalizado='Finalizado'

    MOTOR= 'MOTOR'
    CARROCERIA= 'CARROCERIA'
    ELECTRICO= 'ELECTRICO'
    HIDRAULICO= 'HIDRAULICO'
    CHOICES = (
            (Nuevo, 'Nuevo'),
            (Proceso, 'En Proceso'),
            (Finalizado, 'Finalizado'),
        )
    CHOICES_REPACION = (
            (MOTOR,         'Motor'),
            (CARROCERIA,    'Carroceria'),
            (ELECTRICO,     'Electrico'),
            (HIDRAULICO,    'Hidraulico'),

        )
    id=models.AutoField(primary_key=True)
    detalle=models.CharField(max_length=250, verbose_name='Detalles', null=False)

    estado = models.CharField(
        max_length=20,
        choices=CHOICES,
        default=Nuevo,
        verbose_name='Estado'
    )

    tiporeparacion = models.CharField(
        max_length=20,
        choices=CHOICES_REPACION,
        default=MOTOR,
        verbose_name='Tipo Repación'
    )

    imagen=models.ImageField(upload_to='imagenes/vehiculo/', verbose_name='Imagen',null=True)
    cliente=models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)
    Vehiculo=models.ForeignKey(Vehiculo,null=True,blank=True,on_delete=models.CASCADE)


    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
