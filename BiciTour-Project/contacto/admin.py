from django.contrib import admin
from .models import registroContactanos

# Register your models here.
class AdministrarModeloContactanos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'nombre', 'correo')
    search_fields = ('id', 'nombre', 'correo')
    date_hierarchy = 'created'
    list_filter = ('nombre', 'correo')

admin.site.register(registroContactanos, AdministrarModeloContactanos)
