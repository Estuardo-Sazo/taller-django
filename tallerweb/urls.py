
from django.contrib import admin
from django.urls import path

from clientes import views as clientes_views

from tallerweb import views as local_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',local_views.inicio ,name='inicio'),
    path('clientes/',clientes_views.list_clientes ,name='clientes'),
    path('clientes/nuevo',clientes_views.nuevo_cliente ,name='nuevo_cliente'),


]
