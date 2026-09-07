from django.contrib import admin

from .models import Aviso


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'especie', 'comuna', 'fecha', 'fecha_publicacion')
    list_filter = ('estado', 'especie', 'sexo', 'comuna')
    search_fields = ('nombre', 'comuna', 'sector', 'descripcion', 'contacto')
    ordering = ('-fecha_publicacion',)
