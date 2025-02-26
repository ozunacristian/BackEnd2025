from django.db import models
from django.conf import settings

class Reporte(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # se relaciona el reporte con el proyecto.
    proyecto = models.ForeignKey('proyecto.Proyecto', on_delete=models.CASCADE, related_name='reportes')
    # se relaciona el reporte con el usuario que lo creó.
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reportes_autor')

    def __str__(self):
        return self.titulo

