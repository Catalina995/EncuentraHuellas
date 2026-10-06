from rest_framework import permissions, viewsets

from .models import Aviso
from .permissions import EsDuenoOsoloLectura
from .serializers import AvisoSerializer

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.order_by('-fecha_publicacion')
    serializer_class = AvisoSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        EsDuenoOsoloLectura,
    ]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is None:
        return Response(
            {'error': 'Credenciales invalidas'},
            status=status.HTTP_400_BAD_REQUEST
        )

    token, created = Token.objects.get_or_create(user=user)

    return Response({
        'token': token.key,
        'usuario': user.username,
        'es_administrador': user.is_staff,
    })