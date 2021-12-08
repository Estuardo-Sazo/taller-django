from django.db import models
from ordenestrabajo.models import OrdenTrabajo
# Create your models here.

class Diagnostico(models.Model):
    id=models.AutoField(primary_key=True)
    categoria=models.CharField(max_length=100, verbose_name='Categoría', null=False)
    opcion=models.CharField(max_length=100, verbose_name='Opcion', null=False)
    detalle=models.CharField(max_length=500, verbose_name='Detalles', null=False)

    
    orden=models.ForeignKey(OrdenTrabajo,null=True,blank=True,on_delete=models.CASCADE)


    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
