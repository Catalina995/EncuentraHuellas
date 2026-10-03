from rest_framework.routers import DefaultRouter

from .api_views import AvisoViewSet


router = DefaultRouter()
router.register('avisos', AvisoViewSet, basename='api-avisos')

urlpatterns = router.urls