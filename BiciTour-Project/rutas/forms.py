from django import forms
from .models import RutaRealizada


class RutaRealizadaForm(forms.ModelForm):
    class Meta:
        model = RutaRealizada
        exclude = ['fecha_realizacion']
        widgets = {
            'fecha_realizacion': forms.DateInput(attrs={'type': 'date'}),
        }