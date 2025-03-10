from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Hanya admin yang bisa melakukan perubahan (POST, PUT, DELETE).
    User biasa hanya bisa melakukan GET.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.role == 'admin'
