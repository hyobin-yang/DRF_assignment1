from rest_framework import serializers
from .models import Board
from .models import Comment
from members.models import CustomUser




class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    # user 부분에 nickname 보이게!!

    class Meta:
        model = Comment
        fields = ['id', 'post','user', 'created_at', 'comment']


class BoardSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body', 'comments']
        read_only_fields = ['user']

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data


class UniversitySerializer(serializers.ModelSerializer):
    university = serializers.CharField(source='user.university', read_only=True)

    class Meta:
        model = Board
        fields = ['university', 'id', 'user', 'title', 'body']

    def get_university(self, obj):
        boards = Board.objects.filter(university=obj)
        serializer = BoardSerializer(boards, many=True)
        return serializer.data