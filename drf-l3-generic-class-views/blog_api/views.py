from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostListSerializer, PostSerializer


class PostListView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    permission_classes = [IsAuthorOrReadOnly, ]
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    permission_classes = [IsAuthorOrReadOnly, ]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
