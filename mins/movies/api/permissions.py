from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated, IsAdminUser


class IsAdminUserOrIsOwnerOrReadOnly(BasePermission):
  message = 'You have no permisson to perform this action.'
  def has_object_permission(self, request, view, obj):
    user = request.user
    if request.method in SAFE_METHODS:
      return True
    elif user.is_staff or user.is_superuser:
      return True
    else:
      return obj.author == user
 
class IsAdminUserOrIsUserOrReadOnly(BasePermission):
  message = "Method not allowed on other's data"
  
  def has_object_permission(self, request, view, obj):
    user = request.user
    # Read permissions are allowed to any request,
    if request.method in SAFE_METHODS:
      return True
    # Write permissions are allowed to admin users or the user itself.
    elif user.is_staff or user.is_superuser:
      return True
    else:
      return obj == user