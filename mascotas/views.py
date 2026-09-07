from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .forms import AvisoForm
from .models import Aviso

# Create your views here.
def inicio(request):
    avisos_recientes = Aviso.objects.order_by('-fecha_publicacion')[:4]

    return render(request, 'mascotas/inicio.html', {
        'avisos_recientes': avisos_recientes
    })
    
def avisos(request):
    lista_avisos = Aviso.objects.order_by('-fecha_publicacion')

    busqueda = request.GET.get('buscar')
    especie = request.GET.get('especie')
    estado = request.GET.get('estado')

    if busqueda:
        lista_avisos = lista_avisos.filter(
            Q(nombre__icontains=busqueda) |
            Q(comuna__icontains=busqueda) |
            Q(sector__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        )

    if especie:
        lista_avisos = lista_avisos.filter(especie=especie)

    if estado:
        lista_avisos = lista_avisos.filter(estado=estado)

    return render(request, 'mascotas/avisos.html', {
        'lista_avisos': lista_avisos,
        'total_avisos': lista_avisos.count(),
    })
    
def detalle_aviso(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id)

    return render(request, 'mascotas/detalle_aviso.html', {
        'aviso': aviso
    })
    
def publicar_aviso(request):
    if request.method == 'POST':
        formulario = AvisoForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect('avisos')
    else:
        formulario = AvisoForm()

    return render(request, 'mascotas/publicar_aviso.html', {
        'formulario': formulario
    })


def marcar_reunido(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id)

    if request.method == 'POST':
        aviso.estado = 'reunido'
        aviso.save(update_fields=['estado'])

    return redirect('detalle_aviso', aviso_id=aviso.id)

