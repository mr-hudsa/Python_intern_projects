from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors to edit or delete their own blog posts.
    """
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS — always allow them
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the author can edit/delete
        return obj.author == request.user
