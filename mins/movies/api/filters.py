import django_filters
from movies.models import Movie

class MovieFilter(django_filters.FilterSet):
  rating = django_filters.NumberFilter(field_name='reviews__rating')
  released_date = django_filters.NumberFilter(field_name='released_date', lookup_expr='year')

  class Meta:
    model = Movie
    fields = {
      'title': ['exact', 'icontains'],
      'director': ['exact', 'icontains'],
      'released_date': ['exact'],
    }
