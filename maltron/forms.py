from django import forms
from .models import Contacto
from django.forms import ModelForm

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'