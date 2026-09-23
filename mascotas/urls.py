from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='mascotas/login.html'),
    name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('registro/', views.registro, name='registro'),
    path('avisos/', views.avisos, name='avisos'),
    path('mis-avisos/', views.mis_avisos, name='mis_avisos'),
    path('avisos/<int:aviso_id>/', views.detalle_aviso, name='detalle_aviso'),
    path('avisos/<int:aviso_id>/reunido/', views.marcar_reunido, name='marcar_reunido'),
    path('publicar/', views.publicar_aviso, name='publicar_aviso'),
    path('avisos/<int:aviso_id>/editar/', views.editar_aviso, name='editar_aviso'),
    path('avisos/<int:aviso_id>/eliminar/', views.eliminar_aviso, name='eliminar_aviso'),
]
