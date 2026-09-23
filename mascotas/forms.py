from django import forms
from .models import Aviso
from datetime import date


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
            'fecha': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            ),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Describe color, tamaño, collar, conducta y cualquier seña especial.'
            }),
            'contacto': forms.TextInput(attrs={
                'placeholder': 'Ej: +56 9 1234 5678 o correo@ejemplo.cl'
            }),
        }

        labels = {
            'nombre': 'Nombre de la mascota',
            'imagen': 'Fotografía',
            'fecha': 'Fecha del avistamiento o extravío',
            'contacto': 'Datos de contacto',
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        if fecha and fecha > date.today():
            raise forms.ValidationError(
                'La fecha no puede ser posterior al día de hoy.'
            )

        return fecha
    
    def clean_contacto(self):
        contacto = self.cleaned_data.get('contacto', '').strip()

        if '@' in contacto:
            # Si contiene @, lo validamos como correo electrónico
            validador_email = forms.EmailField()

            try:
                validador_email.clean(contacto)
            except forms.ValidationError:
                raise forms.ValidationError(
                    'Ingresa un correo electrónico válido.'
                )

        else:
            # Si no contiene @, lo tratamos como teléfono
            numeros = ''.join(filter(str.isdigit, contacto))

            if len(numeros) < 8:
                raise forms.ValidationError(
                    'Ingresa un número de teléfono válido o un correo electrónico.'
                )

        return contacto