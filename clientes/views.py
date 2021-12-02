from django.shortcuts import redirect, render
from .forms import ClienteForm
from .models import Cliente

def list_clientes(requets):
    clientes =Cliente.objects.all()
    return render(requets,'clientes/lista.html',{'clientes':clientes})

def nuevo_cliente(request):
    formulario = ClienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request,'clientes/crear.html',{'formulario':formulario})
