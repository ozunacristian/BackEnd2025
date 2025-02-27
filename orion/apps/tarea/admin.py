from django.contrib import admin
from apps.tarea.models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_inicio', 'fecha_vencimiento', 'estado', 'proyecto', 'responsable')
    search_fields = ('titulo', 'descripcion', 'proyecto__titulo', 'responsable__username')
    list_filter = ('estado', 'fecha_inicio', 'fecha_vencimiento', 'proyecto', 'responsable')
