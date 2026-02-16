from rest_framework.response import Response
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    CommentSerializer
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'total number': self.page.paginator.count,
            'next page': self.get_next_link(),
            'previous page': self.get_previous_link(),
            'results': data
        })
    
class PostListAPIView(ListCreateAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all().order_by('created_at')
    pagination_class = CustomPagination

    def create(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def update(self, request):
        post = self.get_object()
        if post.author != request.user:
            return Response(status=status.HTTP_409_CONFLICT)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request):
        post = self.get_object()
        if post.author != request.user:
            return Response(status=status.HTTP_409_CONFLICT)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentListAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['id'])
    
    def create(self, request):
        try:
            post = Post.objects.get(id=self.kwargs['id'])
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
