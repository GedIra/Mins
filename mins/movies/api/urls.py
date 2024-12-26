from django.urls import path
from .views import (
  UserslistAPIView, UserRetrieveUpdateDestroyAPIView, UserRegistrationAPIView, MovieListCreateAPIView,
  MovieRetrieveUpdateDestroyAPIView, ReviewListCreateAPIView
)

urlpatterns = [
  path('api/users/', UserslistAPIView.as_view(), name='users'),
  path('api/user/<str:username>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
  path('api/register/', UserRegistrationAPIView.as_view(), name='register'),
  path('api/movies/', MovieListCreateAPIView.as_view(), name='movies'),
  path('api/movie/<slug:slug>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
  path('api/reviews/', ReviewListCreateAPIView.as_view(), name='reviews'),
]