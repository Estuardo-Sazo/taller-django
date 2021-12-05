from django.forms import fields
from django import forms

from .models import OrdenTrabajo


class OrdenForm(forms.ModelForm):
    class Meta:
        model=OrdenTrabajo
        fields='__all__'