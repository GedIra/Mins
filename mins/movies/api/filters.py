import django_filters
from movies.models import Movie, Review, Comment, Like

class MovieFilter(django_filters.FilterSet):
  rating = django_filters.NumberFilter(field_name='reviews__rating')
  year = django_filters.NumberFilter(field_name='released_date', lookup_expr='year')
  cast = django_filters.CharFilter(field_name='tags__name', lookup_expr='icontains')

  class Meta:
    model = Movie
    fields = {
      'title': ['exact', 'icontains'],
      'director': ['exact', 'icontains'],
      'released_date': ['exact'],
    }

class ReviewFilter(django_filters.FilterSet):
  movie = django_filters.CharFilter(field_name='movie__title', lookup_expr='icontains')
  author = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')
  year = django_filters.NumberFilter(field_name='updated_at', lookup_expr='year')
  
  class Meta:
    model = Review
    fields = {
      'rating' : ['exact'],
      'created_at' : ['exact'],
      'updated_at': ['exact']
    }

class CommnetFilter(django_filters.FilterSet):
  author = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')
  review = django_filters.CharFilter(field_name='review__author__username', lookup_expr='icontains')
  year = django_filters.NumberFilter(field_name='updated_at', lookup_expr='year')
  rating = django_filters.NumberFilter(field_name='review__rating')
  class Meta:
    model = Comment
    fields = {
      'created_at' : ['exact'],
      'updated_at': ['exact']
    }
    
class LikeFilter(django_filters.FilterSet):
  author = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')
  review = django_filters.CharFilter(field_name='review__author__username', lookup_expr='icontains')
  rating = django_filters.NumberFilter(field_name='review__rating')
  class Meta:
    model = Like
    fields = {
      'liked_at' : ['exact'],
      'updated_at': ['exact']
    }