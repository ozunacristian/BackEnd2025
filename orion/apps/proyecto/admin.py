from django.contrib import admin
from apps.proyecto.models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'fecha_actualizacion', 'propietario')
    search_fields = ('titulo', 'descripcion', 'propietario__username')
    list_filter = ('fecha_creacion', 'fecha_actualizacion', 'propietario')
