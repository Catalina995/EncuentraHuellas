from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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
    
@login_required
def publicar_aviso(request):
    if request.method == 'POST':
        formulario = AvisoForm(request.POST, request.FILES)

        if formulario.is_valid():
            aviso = formulario.save(commit=False)
            aviso.usuario = request.user
            aviso.save()
            return redirect('avisos')
    else:
        formulario = AvisoForm()

    return render(request, 'mascotas/publicar_aviso.html', {
        'formulario': formulario
    })


@login_required
@require_POST
def marcar_reunido(request, aviso_id):
    aviso = get_object_or_404(
        Aviso,
        id=aviso_id,
        usuario=request.user
    )

    aviso.estado = 'reunido'
    aviso.save(update_fields=['estado'])

    return redirect('detalle_aviso', aviso_id=aviso.id)

@login_required
def editar_aviso(request, aviso_id):
    aviso = get_object_or_404(
        Aviso,
        id=aviso_id,
        usuario=request.user
    )

    if request.method == 'POST':
        formulario = AvisoForm(
            request.POST,
            request.FILES,
            instance=aviso
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_aviso', aviso_id=aviso.id)

    else:
        formulario = AvisoForm(instance=aviso)

    return render(request, 'mascotas/editar_aviso.html', {
        'formulario': formulario,
        'aviso': aviso
    })
    
    
@login_required
def eliminar_aviso(request, aviso_id):
    aviso = get_object_or_404(
        Aviso,
        id=aviso_id,
        usuario=request.user
    )

    if request.method == 'POST':
        aviso.delete()
        return redirect('avisos')

    return render(request, 'mascotas/eliminar_aviso.html', {
        'aviso': aviso
    })


def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('login')

    else:
        formulario = UserCreationForm()

    return render(request, 'mascotas/registro.html', {
        'formulario': formulario
    })


@login_required
def mis_avisos(request):
    lista_avisos = Aviso.objects.filter(
        usuario=request.user
    ).order_by('-fecha_publicacion')

    return render(request, 'mascotas/mis_avisos.html', {
        'lista_avisos': lista_avisos
    })