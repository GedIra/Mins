from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import (
  Review, Movie, Actor, Comment, Like
)

User = get_user_model()
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ['username', 'email']
  list_filter = ['username']
  ordering = ['username']
  
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
  list_display = ['title', 'released_date', 'director']
  list_filter = ['director', 'released_date']
  ordering = ['title', 'released_date']
  
  def get_queryset(self, request):
    return super().get_queryset(request).prefetch_related('tags')

  def tag_list(self, obj):
    return u", ".join(o.name for o in obj.tags.all())
  

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
  list_display = ['author', 'movie', 'rating']
  list_filter = ['author', 'movie', 'rating']
  ordering = ['movie', 'rating', 'author']
  
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['author', 'review']
  list_filter = ['author', 'review']
  ordering = ['review']
  
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
  list_display = ['author', 'review']
  list_filter = ['review', 'author']
  ordering = ['author']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
  list_display = ['aka', 'name', 'nationality', 'dob']
  list_filter = ['name', 'aka']
  ordering = ['aka']
  search_fields = ['name', 'aka']