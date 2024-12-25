from django.urls import path
from .views import (
  UserslistAPIView
)

urlpatterns = [
  path('api/users/', UserslistAPIView.as_view(), name='users'),
]