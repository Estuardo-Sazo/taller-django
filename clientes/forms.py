from django.forms import fields
from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields='__all__'