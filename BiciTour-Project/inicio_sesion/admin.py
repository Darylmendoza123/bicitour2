from django.contrib import admin
from .models import registroUsuario

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'nombre', 'correo')
    search_fields = ('id', 'nombre', 'correo')
    date_hierarchy = 'created'
    list_filter = ('nombre', 'correo')

admin.site.register(registroUsuario, AdministrarModelo)