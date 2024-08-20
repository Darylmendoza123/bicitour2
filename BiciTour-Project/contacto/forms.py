
from django import forms


from .models import registroContactanos

class registroContactanosForm(forms.ModelForm):
    class Meta:
        model = registroContactanos
        fields = ['nombre', 'apellido', 'correo', 'comentario']