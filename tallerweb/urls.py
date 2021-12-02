
from django.contrib import admin
from django.urls import path

from clientes import views as clientes_views
from vehiculos import views as vehiculos_views

from tallerweb import views as local_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',local_views.login ,name='login'),
    path('inicio/',local_views.inicio ,name='inicio'),
    path('clientes/',clientes_views.list_clientes ,name='clientes'),
    path('vehiculos/<int:id>',vehiculos_views.list_vehiculos_clientes ,name='clientes_vehiculos'),

    path('clientes/nuevo',clientes_views.nuevo_cliente ,name='nuevo_cliente'),


]
