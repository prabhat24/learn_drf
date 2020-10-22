from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostListSerializer, PostSerializer


class PostListView(APIView):
    permission_classes = [IsAuthorOrReadOnly, ]

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        post_serializer = PostListSerializer(queryset, many=True)
        return Response(post_serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailView(APIView):
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        post_object = self.get_object(pk)
        post_serializer = PostSerializer(post_object)
        return Response(post_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        post_object = self.get_object(pk)
        post_serializer = PostSerializer(post_object, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        return Response(post_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        post_object = self.get_object(pk)
        post_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
