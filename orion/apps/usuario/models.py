from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ADMINISTRADOR = 'administrador'
    CREADOR = 'creador'
    MIEMBRO = 'miembro'

    ROLES_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (CREADOR, 'Creador'),
        (MIEMBRO, 'Miembro'),
    ]

    rol = models.CharField(
        max_length=20,
        choices=ROLES_CHOICES,
        default=MIEMBRO,
    )

    def __str__(self):
        return self.username