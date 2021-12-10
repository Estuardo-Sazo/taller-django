from django.shortcuts import redirect, render
from ordenestrabajo.models import OrdenTrabajo
from diagnosticos.models import Diagnostico

from .forms import DiagnosticoForm
# consulta de ordenes de trabajo baso en la relacion cliente vehiculo

def list_ordenes(requets):
    ordenes =OrdenTrabajo.objects.all().select_related('cliente').select_related('Vehiculo')
   
    return render(requets,'diagnosticos/lista.html',{'ordenes':ordenes})

def get_diagnosticos(requets,id):
    orden =OrdenTrabajo.objects.filter(id=id).select_related('cliente').select_related('Vehiculo')
    diagnosticos  =Diagnostico.objects.filter(orden_id=id)
    print(orden)
   
    print(diagnosticos)

    return render(
        request=requets,
        template_name='diagnosticos/ver.html',
        context={
            'orden':orden,
            'diagnosticos':diagnosticos
        }
    )

def nuevo_diagnostico(request,id):
    orden =OrdenTrabajo.objects.filter(id=id).select_related('cliente').select_related('Vehiculo')
    
    formulario = DiagnosticoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('ver-diagnostico',id=id)
    
   # renderiza la vista en el navegador
    return render(
         # enviar variables a la vista html
        request=request,
        template_name='diagnosticos/crear.html',
        context={
            'orden':orden,
            'id':id
        }
    )
