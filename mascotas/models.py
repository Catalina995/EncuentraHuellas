from django.db import models
from django.conf import settings

# Create your models here.
class Aviso(models.Model):
    usuario = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='avisos',
    null=True,
    blank=True
    )
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(
    upload_to='mascotas/',
    blank=True,
    null=True
    )
    especie = models.CharField(
    max_length=20,
    choices=[
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('otro', 'Otro'),
    ]
)
    sexo = models.CharField(
    max_length=20,
    choices=[
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
        ('desconocido', 'Desconocido'),
    ]
)
    estado = models.CharField(
    max_length=20,
    choices=[
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
        ('reunido', 'Reunido con su familia'),
    ]
)
    comuna = models.CharField(max_length=100)
    sector = models.CharField(max_length=150)
    fecha = models.DateField()
    descripcion = models.TextField()
    contacto = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
