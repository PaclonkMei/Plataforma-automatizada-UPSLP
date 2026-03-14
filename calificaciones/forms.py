from django import forms
from .models import Calificacion
from usuarios.models import Usuario

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['alumno', 'materia', 'nota']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alumno'].queryset = Usuario.objects.filter(rol='alumno')