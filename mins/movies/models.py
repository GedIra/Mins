from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUserManager(BaseUserManager):
  def create_user(self, username, email, password= None):
    if not email:
      raise ValueError("The email is required")
    
    user = self.model(username=username, email=self.normalize_email(email))
    
    user.set_password(password)
    user.save(using = self._db)
    return user

  def create_superuser(self, username, email, password=None):
    user = self.create_user(username, email=email, password=password)
    user.is_admin = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user

class CustomUser(AbstractUser):
  email = models.EmailField(verbose_name="email address", unique=True, max_length=255)
  REQUIRED_FIELDS = ['email']
  objects = CustomUserManager()
  
  def __str__(self):
    return self.username

User = get_user_model()

class Movie(models.Model):
  title = models.CharField(max_length=255)
  trailer = models.URLField()
  director = models.CharField(max_length=255)
  released_date = models.DateField()
  summary = models.TextField(blank=True, null=True)
  
  class Meta:
    unique_together = ["title", "released_date"]

class Actor(models.Model):
  name = models.CharField(max_length=255)
  aka = models.CharField(max_length=100, unique=True, blank=True, null=True)
  dob = models.DateField(null=True)
  bio = models.TextField(null=True, blank=True)
  featured_in = models.ManyToManyField(Movie, related_name='actors')
  
class Review(models.Model):
  SCORE_CHOICES = [
    (0, 'Terrible'),
    (1, 'Poor'),
    (2, 'Fair'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
  ]
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
  content = models.TextField()
  rating = models.IntegerField(choices=SCORE_CHOICES)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
  review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
class Like(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
  review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
  liked_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    unique_together = ['author', 'review'] #user can like a riview once