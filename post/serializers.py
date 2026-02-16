from rest_framework import serializers
from .models import Post, Comment
from rest_framework.exceptions import ValidationError

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'body author'.split()


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'title body author'.split()

class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = 'author title body created_at is_published comments'.split()