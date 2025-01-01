from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework_simplejwt.tokens import RefreshToken

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

class IsAdminOrIsOwnRefreshToken(BasePermission):
  #Allows users to blacklist only their own refresh token.
  message = "This refresh token belongs to someone else !!"
  def has_permission(self, request, view):
    user = request.user
    # Extract the refresh token from the request body
    refresh_token = request.data.get('refresh')
    if not refresh_token:
      return False
   
    try:
      # Verify and decode the token
      token = RefreshToken(refresh_token)
      # Check if user is admin
       
      if user.is_staff or user.is_superuser:
        return True
      # Check if the user in the refresh token is the same as the current user
      else: 
        return str(token['user_id']) == str(request.user.id)
    except Exception:
      return False
