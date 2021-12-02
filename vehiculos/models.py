from django.db import models
from clientes.models import Cliente
# Create your models here.

class Vehiculo(models.Model):
    id=models.AutoField(primary_key=True)
    placa=models.CharField(max_length=100, verbose_name='Placa', null=False)
    modelo=models.CharField(max_length=100, verbose_name='Modelo', null=False)
    color=models.CharField(max_length=100, verbose_name='Color', null=False)
    linea=models.CharField(max_length=100, verbose_name='Linea', null=True)
    chasis=models.CharField(max_length=100, verbose_name='No Chasis', null=True)

    cliente=models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)

    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


