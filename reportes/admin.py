from django.contrib import admin
from .models import Reporte

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'fecha_generacion')
    search_fields = ('alumno__username',)
    list_filter = ('fecha_generacion',)