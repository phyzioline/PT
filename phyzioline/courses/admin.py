from django.contrib import admin
from .models import (
    Course, Lesson, CourseMaterial, Enrollment,
    LessonProgress, Certificate, CourseReview
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'trainer', 'price', 'level', 'is_published', 'students_count', 'average_rating']
    list_filter = ['is_published', 'is_featured', 'level', 'is_free']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'duration_minutes', 'is_preview']
    list_filter = ['course', 'is_preview']
    search_fields = ['title', 'description']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'progress_percentage', 'is_completed', 'created_at']
    list_filter = ['is_completed', 'created_at']
    search_fields = ['student__user__username', 'course__title']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['certificate_number', 'enrollment', 'issued_at']
    search_fields = ['certificate_number']


@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['course__title', 'student__user__username']

