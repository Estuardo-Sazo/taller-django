from django.db import models

# Create your models here.
class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombre', null=False)
    apellido=models.CharField(max_length=100, verbose_name='Apellido', null=False)
    correo=models.EmailField(max_length=100, verbose_name='Correo', unique=True)
    telefono=models.CharField(max_length=100, verbose_name='Telefono', null=True)

    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    