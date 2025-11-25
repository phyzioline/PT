from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter
from django.db import transaction, models
from django.utils import timezone
from .models import Course, Lesson, Enrollment, LessonProgress, Certificate, CourseReview
from .serializers import (
    CourseSerializer, LessonSerializer, EnrollmentSerializer,
    LessonProgressSerializer, CertificateSerializer, CourseReviewSerializer
)
from core_data.permissions import IsTrainer, IsOwnerOrReadOnly
from core_data.utils import success_response, error_response


class CourseFilter(FilterSet):
    """فلاتر للكورسات"""
    trainer = NumberFilter(field_name='trainer__id')
    level = CharFilter(field_name='level')
    is_free = BooleanFilter(field_name='is_free')
    is_featured = BooleanFilter(field_name='is_featured')
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    search = CharFilter(method='filter_search')
    
    def filter_search(self, queryset, name, value):
        """بحث في العنوان والوصف"""
        return queryset.filter(
            models.Q(title__icontains=value) |
            models.Q(description__icontains=value)
        )
    
    class Meta:
        model = Course
        fields = ['trainer', 'level', 'is_free', 'is_featured', 'min_price', 'max_price']


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet للكورسات"""
    queryset = Course.objects.filter(is_deleted=False, is_published=True)
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['title', 'description', 'short_description']
    ordering_fields = ['created_at', 'price', 'average_rating']
    ordering = ['-created_at']
    lookup_field = 'slug'
    
    def get_permissions(self):
        """تحديد الصلاحيات"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsTrainer()]
        return [AllowAny()]
    
    def get_queryset(self):
        """تصفية الكورسات"""
        queryset = super().get_queryset()
        
        # إذا كان trainer، يمكنه رؤية جميع كورساته
        if self.action == 'my_courses' and self.request.user.is_authenticated:
            if hasattr(self.request.user, 'userprofile'):
                return Course.objects.filter(
                    trainer=self.request.user.userprofile,
                    is_deleted=False
                )
        
        return queryset
    
    def perform_create(self, serializer):
        """إنشاء كورس جديد"""
        serializer.save(trainer=self.request.user.userprofile)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated, IsTrainer])
    def my_courses(self, request):
        """الحصول على كورسات المدرب الحالي"""
        courses = self.get_queryset()
        serializer = self.get_serializer(courses, many=True)
        return success_response(data=serializer.data)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def enroll(self, request, slug=None):
        """التسجيل في كورس"""
        course = self.get_object()
        student = request.user.userprofile
        
        # التحقق من عدم التسجيل مسبقاً
        if Enrollment.objects.filter(course=course, student=student).exists():
            return error_response(message="أنت مسجل في هذا الكورس بالفعل")
        
        # التحقق من الدفع (إذا كان الكورس مدفوع)
        if not course.is_free and course.price > 0:
            # هنا يمكن إضافة منطق الدفع
            pass
        
        enrollment = Enrollment.objects.create(course=course, student=student)
        serializer = EnrollmentSerializer(enrollment)
        return success_response(
            data=serializer.data,
            message="تم التسجيل في الكورس بنجاح",
            status_code=status.HTTP_201_CREATED
        )


class EnrollmentViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet للتسجيلات"""
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """الحصول على تسجيلات المستخدم الحالي"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            return Enrollment.objects.filter(student=self.request.user.userprofile)
        return Enrollment.objects.none()
    
    @action(detail=True, methods=['patch'])
    def update_progress(self, request, pk=None):
        """تحديث تقدم الطالب"""
        enrollment = self.get_object()
        lesson_id = request.data.get('lesson_id')
        is_completed = request.data.get('is_completed', False)
        
        try:
            lesson = enrollment.course.lessons.get(id=lesson_id)
        except Lesson.DoesNotExist:
            return error_response(message="الدرس غير موجود")
        
        progress, created = LessonProgress.objects.get_or_create(
            enrollment=enrollment,
            lesson=lesson
        )
        
        progress.is_completed = is_completed
        if is_completed:
            progress.completed_at = timezone.now()
        progress.save()
        
        # تحديث نسبة الإنجاز الإجمالية
        total_lessons = enrollment.course.lessons.count()
        completed_lessons = enrollment.lesson_progress.filter(is_completed=True).count()
        enrollment.progress_percentage = int((completed_lessons / total_lessons) * 100) if total_lessons > 0 else 0
        
        if enrollment.progress_percentage == 100:
            enrollment.is_completed = True
            enrollment.completed_at = timezone.now()
            
            # إنشاء شهادة تلقائياً
            if not hasattr(enrollment, 'certificate'):
                Certificate.objects.create(enrollment=enrollment)
        
        enrollment.save()
        
        serializer = EnrollmentSerializer(enrollment)
        return success_response(data=serializer.data, message="تم تحديث التقدم")


class CourseReviewViewSet(viewsets.ModelViewSet):
    """ViewSet لتقييمات الكورسات"""
    serializer_class = CourseReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['course', 'rating', 'is_approved']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على التقييمات الموافق عليها"""
        return CourseReview.objects.filter(is_approved=True)
    
    def perform_create(self, serializer):
        """إنشاء تقييم جديد"""
        serializer.save(student=self.request.user.userprofile)

