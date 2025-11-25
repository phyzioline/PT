from rest_framework import serializers
from .models import Post, Comment, Like, Follow
from accounts.serializers import UserProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    """Serializer للمنشورات"""
    author = UserProfileSerializer(read_only=True)
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id', 'author', 'category', 'category_display', 'content',
            'image', 'video', 'is_published', 'likes_count', 'comments_count',
            'is_liked', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'author', 'likes_count', 'comments_count']
    
    def get_is_liked(self, obj):
        """التحقق من إعجاب المستخدم الحالي"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if hasattr(request.user, 'userprofile'):
                return Like.objects.filter(post=obj, user=request.user.userprofile).exists()
        return False


class CommentSerializer(serializers.ModelSerializer):
    """Serializer للتعليقات"""
    author = UserProfileSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = [
            'id', 'post', 'author', 'parent', 'content', 'likes_count',
            'replies', 'is_liked', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'author', 'likes_count']
    
    def get_replies(self, obj):
        """الحصول على الردود"""
        replies = obj.replies.all()
        return CommentSerializer(replies, many=True, context=self.context).data
    
    def get_is_liked(self, obj):
        """التحقق من إعجاب المستخدم الحالي"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if hasattr(request.user, 'userprofile'):
                return Like.objects.filter(comment=obj, user=request.user.userprofile).exists()
        return False


class LikeSerializer(serializers.ModelSerializer):
    """Serializer للإعجابات"""
    user = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


class FollowSerializer(serializers.ModelSerializer):
    """Serializer للمتابعات"""
    follower = UserProfileSerializer(read_only=True)
    following = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
        read_only_fields = ['id', 'follower', 'created_at']

