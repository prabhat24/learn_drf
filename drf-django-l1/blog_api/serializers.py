from rest_framework import serializers
from .models import Post


# # user = models.ForeignKey()
# title = models.CharField(max_length=20)
# content = models.TextField()
# created = models.DateTimeField(auto_now_add=True)
#
#
# # tag
# class Meta:
#     ordering = 'created'
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ['id', 'title', 'user', 'content']
