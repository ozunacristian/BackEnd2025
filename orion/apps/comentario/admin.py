from django.contrib import admin
from apps.comentario.models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('contenido', 'fecha_creacion', 'tarea', 'autor')
    search_fields = ('contenido', 'tarea__titulo', 'autor__username')
    list_filter = ('fecha_creacion', 'tarea', 'autor')
