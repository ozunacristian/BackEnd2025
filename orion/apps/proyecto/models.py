from django.db import models
from django.conf import settings # se importa settings para poder referenciar al modelo de usuario

class Proyecto(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    # se relaciona el proyecto con el usuario que lo creó.
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='proyectos_propietario')
    # se relaciona el proyecto con los usuarios que participan en él.
    participantes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='proyectos_participantes')

    def __str__(self):
        return self.titulo

