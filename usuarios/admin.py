from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'rol', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Rol del usuario', {'fields': ('rol',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol del usuario', {'fields': ('rol',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)