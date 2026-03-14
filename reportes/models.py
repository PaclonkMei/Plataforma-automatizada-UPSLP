from django.db import models
from usuarios.models import Usuario

class Reporte(models.Model):
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'alumno'})
    contenido = models.TextField()
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reporte de {self.alumno.username} - {self.fecha_generacion.strftime('%d/%m/%Y')}"