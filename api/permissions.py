from rest_framework import permissions
    
class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
    
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        
        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
            
            return obj.author.user == request.user
    
class IsMyProfileOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        if request.user.is_authenticated:
            return obj.user == request.user