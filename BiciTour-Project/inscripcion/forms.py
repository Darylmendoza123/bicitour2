from django import forms
from .models import registroInscripcion

class RegistroInscripcionForm(forms.ModelForm):
    class Meta:
        model = registroInscripcion
        fields = ['nombre', 'correo', 'telefono', 'estado', 'ciudad'] 