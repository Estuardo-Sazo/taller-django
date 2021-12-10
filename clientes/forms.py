from django.forms import fields
from django import forms

from .models import Cliente
# solo para crear  formularios en base al modelo

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields='__all__'
