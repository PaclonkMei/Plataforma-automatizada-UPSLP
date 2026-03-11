from django.db import models
from usuarios.models import Usuario

class Calificacion(models.Model):
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'alumno'})
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='calificaciones_asignadas', limit_choices_to={'rol': 'profesor'})
    materia = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno.username} - {self.materia}: {self.nota}"