from rest_framework.permissions import BasePermission

class AllowAnyOnGet(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            if request.user.is_authenticated:
                return True
        return False
