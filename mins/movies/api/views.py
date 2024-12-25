from .serializers import (
  UserSerializer, UserRegistrationSerializer, ReviewSerializer,
  CommentSerializer, LikeSerializer, MovieSerializer, User
)
from movies.models import (
  Movie, Review, Comment, Like
)

from rest_framework import generics
from django.contrib.auth.decorators import user_passes_test
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (
  IsAuthenticated, IsAdminUser, SAFE_METHODS,
  DjangoModelPermissionsOrAnonReadOnly
  )

class  UserRegistrationAPIView(generics.CreateAPIView):
  serializer_class = UserRegistrationSerializer
  queryset = User.objects.all()

  def perform_create(self, serializer):
    # Check if there is already a SignupRequest for the current user
    queryset = User.objects.filter(user=self.request.user)
    if queryset.exists():
      # If a SignupRequest exists, raise a ValidationError to prevent duplicate sign-ups
      raise ValidationError('You have already signed up')
    # Save the serializer with the current user associated to the SignupRequest
    serializer.save(user=self.request.user)
    return super().perform_create(serializer)

class UserslistAPIView(generics.ListAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  permission_classes = []
  authentication_classes = []

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = UserSerializer
  permission_classes = []
  authentication_classes = []
  def get_queryset(self):
    user = self.request.user 
    return User.objects.get(username = user.username)
  
  
class MovieListCreateAPIView(generics.ListCreateAPIView):
  serializer_class = MovieSerializer
  queryset = Movie.objects.all()
  permission_classes = []
  authentication_classes = []

  def get_permissions(self):
    if self.request.method == 'POST':
      # Only admin users can create movies
      self.permission_classes = [IsAdminUser]
    else:
      # All users can retrieve and list movies
      self.permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    return super().get_permissions()

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = MovieSerializer
  queryset = Movie.objects.all()
  permission_classes = []
  authentication_classes = []

  def get_permissions(self):
    if self.request.method in SAFE_METHODS:
      # All users can retrieve and list movies
      self.permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    else:
      # Only admin users can update or delete movies
      self.permission_classes = [IsAdminUser]
    return super().get_permissions()
  
  
class ReviewListCreateAPIView(generics.ListCreateAPIView):
  serializer_class = ReviewSerializer
  queryset = Review.objects.all()
  permission_classes = []
  authentication_classes = []
    
  def perform_create(self, serializer):
    #sets Review auhtor to the currrent user
    serializer.save(author = self.request.author)
    return super().perform_create(serializer)

  
class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ReviewSerializer
  permission_classes = []
  authentication_classes = []
  
  def get_queryset(self):
    user = self.request.user
    return Review.objects.filter(author = user)
  
  def perform_update(self, serializer):
    #sets Review auhtor to the currrent user
    serializer.save(author = self.request.author)
    return super().perform_update(serializer)

class CommentListCreateAPIView(generics.ListCreateAPIView):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  permission_classes = []
  authentication_classes = []
  
  def perform_create(self, serializer):
    #sets Comment auhtor to the currrent user
    serializer.save(author = self.request.author)
    return super().perform_create(serializer)
  
class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = CommentSerializer
  permission_classes = []
  authentication_classes = []
  
  def get_queryset(self):
    user = self.request.user
    return Comment.objects.filter(author = user)
  
  def perform_update(self, serializer):
    #sets Comment auhtor to the currrent user
    serializer.save(author = self.request.author)
    return super().perform_update(serializer)
  
class LikeListCreateAPIView(generics.ListCreateAPIView):
  serializer_class = LikeSerializer
  queryset = Like.objects.all()
  permission_classes = []
  authentication_classes = []
  
  def perform_create(self, serializer):
    serializer.save(author = self.request.user)
    return super().perform_create(serializer)
  
class LikeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = LikeSerializer
  permission_classes = []
  authentication_classes = []
  
  def get_queryset(self):
    user = self.request.user
    return Like.objects.filter(author = user)
  
  def perform_update(self, serializer):
    serializer.save(author = self.request.user)
    return super().perform_update(serializer)
  
  def perform_destroy(self, instance):
    return super().perform_destroy(instance)