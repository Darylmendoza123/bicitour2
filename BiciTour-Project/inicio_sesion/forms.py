from django import forms

from .models import registroUsuario

class registroUsuarioForm(forms.ModelForm):
    class Meta:
        model = registroUsuario
        fields = ['correo', 'nombre', 'contraseña']