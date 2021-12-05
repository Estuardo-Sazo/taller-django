from django.shortcuts import render
from ordenestrabajo.models import OrdenTrabajo
# Create your views here.

def list_ordenes(requets):
    ordenes =OrdenTrabajo.objects.all()
    return render(requets,'ordenes/lista.html',{'ordenes':ordenes})

def nueva_orden(request):
    return render(request,'ordenes/create.html') 
