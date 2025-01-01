from django.urls import path
from .views import (
  UserslistAPIView, UserRetrieveUpdateDestroyAPIView, UserRegistrationAPIView, MovieListCreateAPIView,
  MovieRetrieveUpdateDestroyAPIView, ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView,
  CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView, LikeListCreateAPIView, LikeRetrieveUpdateDestroyAPIView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView


urlpatterns = [
  path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/logout/', TokenBlacklistView().as_view(), name='token_blacklist'),
  path('api/users/', UserslistAPIView.as_view(), name='users'),
  path('api/user/<str:username>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
  path('api/register/', UserRegistrationAPIView.as_view(), name='register'),
  path('api/movies/', MovieListCreateAPIView.as_view(), name='movies'),
  path('api/movie/<slug:slug>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
  path('api/reviews/', ReviewListCreateAPIView.as_view(), name='reviews'),
  path('api/review/<slug:slug>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
  path('api/comments/', CommentListCreateAPIView.as_view(), name='comments'),
  path('api/comment/<slug:slug>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
  path('api/likes/', LikeListCreateAPIView.as_view(), name='likes'),
  path('api/like/<slug:slug>/', LikeRetrieveUpdateDestroyAPIView.as_view(), name='like-detail'),
]