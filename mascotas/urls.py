from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('avisos/', views.avisos, name='avisos'),
    path('avisos/<int:aviso_id>/', views.detalle_aviso, name='detalle_aviso'),
    path('avisos/<int:aviso_id>/reunido/', views.marcar_reunido, name='marcar_reunido'),
    path('publicar/', views.publicar_aviso, name='publicar_aviso'),
]
