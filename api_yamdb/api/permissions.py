from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    def has_permission(self, request, view):
        return (not request.user.is_anonymous and
                request.user.role == 'admin' or request.user.is_superuser)
