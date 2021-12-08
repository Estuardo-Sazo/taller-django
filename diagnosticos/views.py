from django.shortcuts import redirect, render
from ordenestrabajo.models import OrdenTrabajo
from diagnosticos.models import Diagnostico

# Create your views here.
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