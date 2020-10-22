from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'user', 'content', 'slug']
