from rest_framework import serializers

from .models import Aviso


class AvisoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Aviso
        fields = [
            'id',
            'usuario',
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
            'fecha_publicacion',
        ]
        read_only_fields = [
            'id',
            'usuario',
            'fecha_publicacion',
        ]