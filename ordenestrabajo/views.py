from django.shortcuts import redirect, render
from ordenestrabajo.models import OrdenTrabajo
from .forms import OrdenForm
# Create your views here.

def list_ordenes(requets):
    ordenes =OrdenTrabajo.objects.all()
    return render(requets,'ordenes/lista.html',{'ordenes':ordenes})

def nueva_orden(request):
    formulario = OrdenForm(request.POST or None, request.FILES or None)
    print(formulario)
    if formulario.is_valid():
        formulario.save()
        return redirect('ordenes')

    return render(
        request=request,
        template_name='ordenes/create.html',
        context={
            'formulario':formulario
        }
    ) 
