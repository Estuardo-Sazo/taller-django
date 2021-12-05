
from django.contrib import admin
from django.urls import path

from clientes import views as clientes_views
from vehiculos import views as vehiculos_views
from ordenestrabajo import views as ordens_views
from tallerweb import views as local_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',local_views.login ,name='login'),
    path('inicio/',local_views.inicio ,name='inicio'),
    
    path('vehiculos/<int:id>',vehiculos_views.list_vehiculos_clientes ,name='clientes_vehiculos'),
    path('crear-vehiculos/<int:idCliente>',vehiculos_views.nuevo_vehiculo ,name='crear_vehiculo'),
    path('vehiculos/q/<int:id>',vehiculos_views.get_vehiculos_clientes ,name='buscar_vehiculos'),
    

    path('ordenes/',ordens_views.list_ordenes ,name='ordenes'),
    path('nueva-orden/',ordens_views.nueva_orden ,name='nueva_orden'),


    path('clientes/',clientes_views.list_clientes ,name='clientes'),
    path('clientes/nuevo',clientes_views.nuevo_cliente ,name='nuevo_cliente'),
    path('clientes/q/<str:search>',clientes_views.cliente_search ,name='buscar_cliente'),



]
