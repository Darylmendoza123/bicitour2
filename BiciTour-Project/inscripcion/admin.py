from django.contrib import admin
from .models import registroInscripcion

class AdministrarModeloInscripcion(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
   

admin.site.register(registroInscripcion, AdministrarModeloInscripcion)
