from django.db import models
from django.conf import settings
from apps.proyecto.models import Proyecto

class Tarea(models.Model):
    # Posibles estados de una tarea definidas en constantes para evitar errores de tipeo.
    PENDIENTE = 'pendiente'
    EN_PROGRESO = 'en_progreso'
    COMPLETADA = 'completada'

    ESTADO_CHOICES = [
        (PENDIENTE, 'Pendiente'),
        (EN_PROGRESO, 'En Progreso'),
        (COMPLETADA, 'Completada'),
    ]

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default=PENDIENTE,
    )
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tareas_responsable')

    def __str__(self):
        return self.titulo

