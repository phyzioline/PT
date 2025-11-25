from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
from core_data.models import TimeStampedModel, SoftDeleteModel


# =================================================================
# 1. المنشورات (Posts)
# =================================================================
class Post(TimeStampedModel, SoftDeleteModel):
    """المنشورات في Feed"""
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts', verbose_name="المؤلف")
    
    category = models.CharField(
        max_length=20,
        choices=[
            ('devices', 'أجهزة'),
            ('courses', 'كورسات'),
            ('jobs', 'وظائف'),
            ('clinics', 'عيادات'),
            ('sessions', 'جلسات'),
            ('general', 'عام'),
        ],
        default='general',
        verbose_name="الفئة"
    )
    
    content = models.TextField(verbose_name="المحتوى")
    image = models.ImageField(upload_to='feed/images/', blank=True, null=True, verbose_name="صورة")
    video = models.FileField(upload_to='feed/videos/', blank=True, null=True, verbose_name="فيديو")
    
    is_published = models.BooleanField(default=True, verbose_name="منشور؟")
    likes_count = models.PositiveIntegerField(default=0, verbose_name="عدد الإعجابات")
    comments_count = models.PositiveIntegerField(default=0, verbose_name="عدد التعليقات")
    
    class Meta:
        verbose_name = "منشور"
        verbose_name_plural = "المنشورات"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Post by {self.author.user.username}"


# =================================================================
# 2. التعليقات (Comments)
# =================================================================
class Comment(TimeStampedModel):
    """تعليقات على المنشورات"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="المنشور")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments', verbose_name="المؤلف")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name="رد على")
    
    content = models.TextField(verbose_name="المحتوى")
    likes_count = models.PositiveIntegerField(default=0, verbose_name="عدد الإعجابات")
    
    class Meta:
        verbose_name = "تعليق"
        verbose_name_plural = "التعليقات"
        ordering = ['created_at']
    
    def __str__(self):
        return f"Comment by {self.author.user.username}"


# =================================================================
# 3. الإعجابات (Likes)
# =================================================================
class Like(models.Model):
    """الإعجابات على المنشورات والتعليقات"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='likes', verbose_name="المستخدم")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='likes', verbose_name="المنشور")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='likes', verbose_name="التعليق")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإعجاب")
    
    class Meta:
        verbose_name = "إعجاب"
        verbose_name_plural = "الإعجابات"
        unique_together = [
            ['user', 'post'],
            ['user', 'comment'],
        ]
    
    def __str__(self):
        if self.post:
            return f"Like on post by {self.user.user.username}"
        return f"Like on comment by {self.user.user.username}"


# =================================================================
# 4. المتابعون (Follows)
# =================================================================
class Follow(models.Model):
    """نظام المتابعة"""
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following', verbose_name="المتابع")
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followers', verbose_name="المتابَع")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ المتابعة")
    
    class Meta:
        verbose_name = "متابعة"
        verbose_name_plural = "المتابعات"
        unique_together = ['follower', 'following']
    
    def __str__(self):
        return f"{self.follower.user.username} follows {self.following.user.username}"

