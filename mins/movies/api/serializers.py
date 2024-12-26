from rest_framework import serializers
from movies.models import Movie, Review, Comment, Like
from django.contrib.auth import get_user_model
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.utils.text import slugify
User = get_user_model()

class MovieSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
  tags = TagListSerializerField(write_only = True)
  class Meta:
    model = Movie
    fields = '__all__'
    read_only_fields = ['slug']
    extra_kwargs = {
      'tags': {'write_only': True}, #to avoid being displayed in the output
      'url': {'view_name': 'movie-detail', 'lookup_field': 'slug'}
    }
  
  def validate(self, attrs): #Overriding the validate method to automatically generate the slug.
    title = attrs.get('title', '')
    released_date = attrs.get('released_date', None)
    if not released_date:
      raise serializers.ValidationError("Released date is required to generate the slug.")

    publication_year = released_date.year
    slug = slugify(f"{title} {publication_year}")
    attrs['slug'] = slug
    return attrs
    

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'url']
    extra_kwargs = {
      'password':{'write_only': True}, #to avoid being displayed in the output
      'url': {'view_name': 'user-detail', 'lookup_field': 'username'},
    }
    
  def update(self, instance, validated_data):
    # Update the password if provided
    password = validated_data.pop('password', None)
    user = super().update(instance, validated_data)
    if password:
      user.set_password(password) #harshing the password with set_password method
      user.save()
    return user

class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'email', 'username', 'password']
    extra_kwargs = {
      'password':{'write_only': True},
      'url': {'view_name': 'user-detail', 'lookup_field': 'username'}
    }
    
  def create(self, validated_data):
    user = User.objects.create_user( #create_user handles user creation and password harshing
      email = validated_data['email'],
      username = validated_data['username'],
      password = validated_data['password']
    )
    return user
  
  
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
  author_username = serializers.CharField(source='author.username', read_only=True)
  class Meta:
    model = Review
    fields = ['url', 'author_username', 'author', 'content', 'rating', 'created_at', 'updated_at']
    read_only_fields = ['author', 'author_username', 'url']
    depth = 1
    
class CommentSerializer(serializers.HyperlinkedModelSerializer):
  author_username = serializers.CharField(source='author.username', read_only=True)
  
  class Meta:
    model = Comment
    fields = ['url', 'author_username', 'author', 'review', 'content', 'created_at', 'updated_at']
    read_only_fields = ['author', 'url', 'author_username']
    
class LikeSerializer(serializers.HyperlinkedModelSerializer):
  author_username = serializers.CharField(source='author.username', read_only=True)
  class Meta:
    model = Like
    fields = ['url', 'author_username', 'author', 'review', 'content', 'liked_at', 'updated_at']
    read_only_fields = ['author', 'url', 'author_username']