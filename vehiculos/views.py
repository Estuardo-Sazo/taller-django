from django.shortcuts import render,redirect
from vehiculos.models import Vehiculo
from clientes.models import Cliente
from django.http.response import JsonResponse

from .forms import VehiculoForm

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

def get_vehiculos_clientes(requets,id):
    vehiculos  =Vehiculo.objects.filter(cliente_id=id).values()
    response={
            'vehiculos':list(vehiculos)
        }
    return JsonResponse(response)


def nuevo_vehiculo(request,idCliente):
    cliente = Cliente.objects.get(id=idCliente)
    formulario = VehiculoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')

    return render(
        request=request,
        template_name='vehiculos/crear.html',
        context={
            'formulario':formulario,
            'cliente':cliente
        }
    )    

