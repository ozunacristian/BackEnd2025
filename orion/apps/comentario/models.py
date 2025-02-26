from django.db import models
from django.conf import settings

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tarea = models.ForeignKey('tarea.Tarea', on_delete=models.CASCADE, related_name='comentario')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentario_autor')

    def __str__(self):
        return f'Comentario de {self.autor} en {self.tarea}'