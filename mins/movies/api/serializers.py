from rest_framework import serializers
from movies.models import Movie, Review, Comment, Like
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {'password':{'write_only': True}} #to avoid being displayed in the output
    
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
    extra_kwargs = {'password':{'write_only': True}}
    
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