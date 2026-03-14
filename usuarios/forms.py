from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

Usuario = get_user_model()

class UsuarioForm(forms.ModelForm):
    # Campo rol con opciones predefinidas
    rol = forms.ChoiceField(
        choices=[
            ('alumno', 'Alumno'),
            ('profesor', 'Profesor'),
            ('coordinador', 'Coordinador'),
            ('administrador', 'Administrador')
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        label='Rol'
    )
    
    # Campos de contraseña (solo para crear nuevos usuarios)
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        help_text='Mínimo 8 caracteres'
    )
    
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'rol']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        # Detectar si es creación o edición
        self.is_new = kwargs.get('instance') is None
        super().__init__(*args, **kwargs)
        
        # Si es creación, hacer contraseñas obligatorias
        if self.is_new:
            self.fields['password1'].required = True
            self.fields['password2'].required = True
        else:
            # Si es edición, remover campos de contraseña
            del self.fields['password1']
            del self.fields['password2']
    
    def clean(self):
        cleaned_data = super().clean()
        
        # Validar contraseñas solo si es nuevo usuario
        if self.is_new:
            password1 = cleaned_data.get('password1')
            password2 = cleaned_data.get('password2')
            
            if password1 and password2:
                if password1 != password2:
                    raise ValidationError('Las contraseñas no coinciden.')
                
                if len(password1) < 8:
                    raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Asignar contraseña solo si es nuevo usuario
        if self.is_new:
            user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        
        return user