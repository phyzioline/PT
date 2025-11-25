from rest_framework import serializers
from django.db import models
from .models import (
    Course, Lesson, CourseMaterial, Enrollment,
    LessonProgress, Certificate, CourseReview
)
from accounts.serializers import UserProfileSerializer


class CourseMaterialSerializer(serializers.ModelSerializer):
    """Serializer للمواد التعليمية"""
    class Meta:
        model = CourseMaterial
        fields = ['id', 'title', 'file', 'file_type']
        read_only_fields = ['id']


class LessonSerializer(serializers.ModelSerializer):
    """Serializer للدروس"""
    materials = CourseMaterialSerializer(many=True, read_only=True)
    
    class Meta:
        model = Lesson
        fields = [
            'id', 'course', 'title', 'description', 'video_url', 'video_file',
            'duration_minutes', 'order', 'is_preview', 'materials', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class CourseSerializer(serializers.ModelSerializer):
    """Serializer للكورسات"""
    trainer = UserProfileSerializer(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    lessons_count = serializers.IntegerField(source='lessons.count', read_only=True)
    level_display = serializers.CharField(source='get_level_display', read_only=True)
    enrollments_count = serializers.IntegerField(source='enrollments.count', read_only=True)
    is_enrolled = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = [
            'id', 'trainer', 'title', 'slug', 'description', 'short_description',
            'price', 'is_free', 'thumbnail', 'duration_hours', 'level', 'level_display',
            'is_published', 'is_featured', 'students_count', 'average_rating',
            'lessons', 'lessons_count', 'enrollments_count', 'is_enrolled',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'trainer']
    
    def get_is_enrolled(self, obj):
        """التحقق من تسجيل المستخدم الحالي"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if hasattr(request.user, 'userprofile'):
                return Enrollment.objects.filter(
                    course=obj,
                    student=request.user.userprofile
                ).exists()
        return False


class EnrollmentSerializer(serializers.ModelSerializer):
    """Serializer للتسجيلات"""
    course = CourseSerializer(read_only=True)
    student = UserProfileSerializer(read_only=True)
    certificate = serializers.SerializerMethodField()
    
    class Meta:
        model = Enrollment
        fields = [
            'id', 'course', 'student', 'progress_percentage',
            'completed_at', 'is_completed', 'certificate', 'created_at'
        ]
        read_only_fields = ['id', 'student', 'created_at']
    
    def get_certificate(self, obj):
        """الحصول على الشهادة إن وجدت"""
        if hasattr(obj, 'certificate'):
            return CertificateSerializer(obj.certificate).data
        return None


class LessonProgressSerializer(serializers.ModelSerializer):
    """Serializer لتقدم الطالب"""
    lesson = LessonSerializer(read_only=True)
    
    class Meta:
        model = LessonProgress
        fields = [
            'id', 'enrollment', 'lesson', 'is_completed',
            'watched_duration', 'completed_at'
        ]
        read_only_fields = ['id']


class CertificateSerializer(serializers.ModelSerializer):
    """Serializer للشهادات"""
    enrollment = EnrollmentSerializer(read_only=True)
    
    class Meta:
        model = Certificate
        fields = ['id', 'enrollment', 'certificate_number', 'issued_at', 'created_at']
        read_only_fields = ['id', 'created_at']


class CourseReviewSerializer(serializers.ModelSerializer):
    """Serializer لتقييمات الكورسات"""
    student = UserProfileSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    
    class Meta:
        model = CourseReview
        fields = [
            'id', 'course', 'student', 'enrollment', 'rating',
            'comment', 'is_approved', 'created_at'
        ]
        read_only_fields = ['id', 'student', 'is_approved', 'created_at']

