from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.core.exceptions import ValidationError

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
  slug = models.SlugField(unique=True, blank=True, null=True)
  tags = TaggableManager()

  class Meta:
    unique_together = ["title", "released_date"]

  def clean(self):
    super().clean()  # Ensure any parent class validation logic is executed first
    # Check if a movie with the same title and release year exists
    year = self.released_date.year
    if Movie.objects.filter(title=self.title, released_date__year=year).exclude(pk=self.pk).exists():
      raise ValidationError('No movies of the same title can be released in the same year')

  def save(self, *args, **kwargs):
    self.publication_year = self.released_date.year
    self.slug = slugify(f"{self.title} {self.publication_year}")
    self.full_clean()  # This calls clean and ensures all validation is done
    return super().save(*args, **kwargs)

  def __str__(self):
    return self.title

class Actor(models.Model):
  name = models.CharField(max_length=255)
  aka = models.CharField(max_length=100, unique=True, blank=True, null=True)
  dob = models.DateField(null=True)
  nationality = CountryField(blank=True, null=True)
  bio = models.TextField(null=True, blank=True)
  featured_in = models.ManyToManyField(Movie, related_name='cast')
  
  def __str__(self):
    return self.aka
  
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
  slug = models.SlugField(unique=True, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    unique_together = ['author', 'movie'] #User can create one review per movie

  def save(self, *args, **kwargs):
    self.slug = slugify(f"{self.author} {self.movie.slug}")
    self.full_clean()  # This calls clean and ensures all validation is done
    return super().save(*args, **kwargs)
  
  def __str__(self):
    return f'{self.rating} star review on {self.movie.title} by {self.author}'
  
class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
  review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
  content = models.TextField()
  slug = models.SlugField(unique=True, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

  def save(self, *args, **kwargs): #creating a slugs by appendeding authors review comments Counts at the end
    # Generate initial slug
    num = 1
    slug = slugify(f"{self.author} {self.review.slug}")
    base_slug = slug
    # Ensure uniqueness of the slug
    while Comment.objects.filter(slug=slug).exclude(pk=self.pk).exists():
      num += 1
      slug = slugify(f"{base_slug}-{num}")

    self.slug = slug
    self.full_clean()  # This calls clean and ensures all validation is done
    return super().save(*args, **kwargs)
  
  def __str__(self):
    return f"{self.author} comment on {self.review}"
  
class Like(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
  review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
  slug = models.SlugField(unique=True, null=True, blank=True)
  liked_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ['author', 'review'] #user can like a riview once
    
  def save(self, *args, **kwargs):
    self.slug = slugify(f"{self.author}-{self.review.slug}")
    return super().save(*args, **kwargs)