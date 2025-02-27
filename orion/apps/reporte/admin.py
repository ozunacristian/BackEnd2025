from django.contrib import admin
from apps.reporte.models import Reporte

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_creacion', 'proyecto', 'autor')
    search_fields = ('titulo', 'descripcion', 'proyecto__titulo', 'autor__username')
    list_filter = ('fecha_creacion', 'proyecto', 'autor')
