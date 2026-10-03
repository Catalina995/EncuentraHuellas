from rest_framework import permissions, viewsets

from .models import Aviso
from .permissions import EsDuenoOsoloLectura
from .serializers import AvisoSerializer


class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.order_by('-fecha_publicacion')
    serializer_class = AvisoSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        EsDuenoOsoloLectura,
    ]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)