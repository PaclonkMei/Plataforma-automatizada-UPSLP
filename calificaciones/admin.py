from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'profesor', 'materia', 'nota', 'fecha')
    list_filter = ('materia', 'profesor')
    search_fields = ('alumno__username', 'materia')