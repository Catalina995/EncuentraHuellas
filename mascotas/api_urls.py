from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api_views import AvisoViewSet, api_login

router = DefaultRouter()
router.register('avisos', AvisoViewSet, basename='api-avisos')

urlpatterns = [
    path('login/', api_login, name='api_login'),
    path('', include(router.urls)),
]