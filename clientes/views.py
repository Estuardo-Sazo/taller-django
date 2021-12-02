from django.shortcuts import redirect, render
from .forms import ClienteForm
clientes=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

def list_clientes(requets):
    return render(requets,'clientes/lista.html',{'clientes':clientes})

def nuevo_cliente(request):
    formulario = ClienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request,'clientes/crear.html',{'formulario':formulario})
