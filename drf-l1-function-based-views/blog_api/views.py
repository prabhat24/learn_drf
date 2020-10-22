from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostListSerializer, PostSerializer
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST'])
def post_list_view(request):
    if request.method == 'GET':
        queryset = Post.objects.all()
        post_serializer = PostListSerializer(queryset, many=True)
        return Response(post_serializer.data)

    else:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthorOrReadOnly, ])
def post_detail_view(request, pk):
    def get_object(pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    post_obj = get_object(pk)
    if request.method == 'GET':
        post_serializer = PostSerializer(post_obj)
        return Response(post_serializer.data)

    elif request.method == 'PUT':
        post_serializer = PostSerializer(post_obj, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(post_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
