from django import forms
from .models import Aviso


class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = [
            'nombre',
            'imagen',
            'especie',
            'sexo',
            'estado',
            'comuna',
            'sector',
            'fecha',
            'descripcion',
            'contacto',
        ]
        
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Describe color, tamaño, collar, conducta y cualquier seña especial.'
            }),
            'contacto': forms.TextInput(attrs={
                'placeholder': 'Teléfono, WhatsApp o correo de contacto'
            }),
        }

        labels = {
            'nombre': 'Nombre de la mascota',
            'imagen': 'Fotografía',
            'fecha': 'Fecha del avistamiento o extravío',
            'contacto': 'Datos de contacto',
        }
