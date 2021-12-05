from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from clientes.forms import ClienteForm
from clientes.models import Cliente
import json
from django.http import HttpResponse

def list_clientes(requets):
    clientes =Cliente.objects.all()
    return render(requets,'clientes/lista.html',{'clientes':clientes})

def nuevo_cliente(request):
    formulario = ClienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request,'clientes/crear.html',{'formulario':formulario})

def cliente_search(request,search):            
        clientes=Cliente.objects.filter(nombre__contains=search).values()
        response={
            'clientes':list(clientes)
        }
        return JsonResponse(response)


