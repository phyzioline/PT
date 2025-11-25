from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from accounts.models import UserProfile
from .models import Post, Comment, Like, Follow
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, FollowSerializer
from core_data.utils import success_response, error_response


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet للمنشورات"""
    queryset = Post.objects.filter(is_deleted=False, is_published=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['content']
    ordering_fields = ['created_at', 'likes_count']
    ordering = ['-created_at']
    
    def perform_create(self, serializer):
        """إنشاء منشور جديد"""
        serializer.save(author=self.request.user.userprofile)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        """إعجاب/إلغاء إعجاب"""
        post = self.get_object()
        user_profile = request.user.userprofile
        
        like, created = Like.objects.get_or_create(user=user_profile, post=post)
        if not created:
            like.delete()
            post.likes_count = max(0, post.likes_count - 1)
            message = "تم إلغاء الإعجاب"
        else:
            post.likes_count += 1
            message = "تم الإعجاب"
        
        post.save()
        return success_response(message=message)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def feed(self, request):
        """Feed المستخدم (منشورات المتابعين)"""
        user_profile = request.user.userprofile
        following_ids = Follow.objects.filter(follower=user_profile).values_list('following_id', flat=True)
        following_ids = list(following_ids) + [user_profile.id]  # إضافة منشورات المستخدم نفسه
        
        posts = Post.objects.filter(
            author_id__in=following_ids,
            is_deleted=False,
            is_published=True
        ).order_by('-created_at')[:50]
        
        serializer = self.get_serializer(posts, many=True)
        return success_response(data=serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet للتعليقات"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['post', 'author']
    ordering_fields = ['created_at']
    ordering = ['created_at']
    
    def get_queryset(self):
        """الحصول على التعليقات"""
        post_id = self.request.query_params.get('post')
        if post_id:
            return Comment.objects.filter(post_id=post_id, parent=None)
        return Comment.objects.all()
    
    def perform_create(self, serializer):
        """إنشاء تعليق جديد"""
        serializer.save(author=self.request.user.userprofile)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        """إعجاب/إلغاء إعجاب تعليق"""
        comment = self.get_object()
        user_profile = request.user.userprofile
        
        like, created = Like.objects.get_or_create(user=user_profile, comment=comment)
        if not created:
            like.delete()
            comment.likes_count = max(0, comment.likes_count - 1)
            message = "تم إلغاء الإعجاب"
        else:
            comment.likes_count += 1
            message = "تم الإعجاب"
        
        comment.save()
        return success_response(message=message)


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSet للمتابعات"""
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['follower', 'following']
    
    def get_queryset(self):
        """الحصول على المتابعات"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            return Follow.objects.filter(follower=self.request.user.userprofile)
        return Follow.objects.none()
    
    def perform_create(self, serializer):
        """إنشاء متابعة جديدة"""
        serializer.save(follower=self.request.user.userprofile)
    
    @action(detail=False, methods=['post'], url_path='toggle')
    def toggle_follow(self, request):
        """تبديل المتابعة"""
        following_id = request.data.get('following_id')
        if not following_id:
            return error_response(message="following_id مطلوب")
        
        try:
            following = UserProfile.objects.get(id=following_id)
        except UserProfile.DoesNotExist:
            return error_response(message="المستخدم غير موجود")
        
        follower = request.user.userprofile
        follow, created = Follow.objects.get_or_create(follower=follower, following=following)
        
        if not created:
            follow.delete()
            message = "تم إلغاء المتابعة"
        else:
            message = "تمت المتابعة"
        
        return success_response(message=message)

