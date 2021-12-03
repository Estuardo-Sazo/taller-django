from django.shortcuts import render,redirect
from vehiculos.models import Vehiculo
from clientes.models import Cliente

# Create your vie ws here.
def list_vehiculos_clientes(requets,id):
    cliente = Cliente.objects.get(id=id)
    vehiculos  =Vehiculo.objects.filter(cliente_id=id)
    print(vehiculos)
    return render(
        request=requets,
        template_name='vehiculos/lista.html',
        context={
            'vehiculos':vehiculos,
            'cliente':cliente
        }
    )