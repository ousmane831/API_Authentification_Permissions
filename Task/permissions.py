from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Autoriser les requêtes en lecture pour tout le monde (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Autoriser les modifications seulement au propriétaire
        return obj.owner == request.user
