from django.contrib import admin
from apps.usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('rol', 'is_staff', 'is_superuser', 'is_active')
