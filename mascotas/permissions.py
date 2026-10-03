from rest_framework import permissions


class EsDuenoOsoloLectura(permissions.BasePermission):
    """
    Permite lectura a cualquier usuario, pero solo el dueño
    del aviso puede editarlo o eliminarlo.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.usuario == request.user