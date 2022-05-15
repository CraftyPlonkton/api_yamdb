from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrSuperuserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin' or request.user.is_superuser


class IsAdminOrModeratorOrOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return (request.user.is_superuser or
                request.user.role == 'admin' or
                request.user.role == 'moderator' or
                request.user.username == obj.author.username)


class IsAdminOrModeratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return (request.user.is_superuser or
                request.user.role == 'admin' or
                request.user.role == 'moderator')


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return (request.user.is_superuser or
                request.user.role == 'admin')
