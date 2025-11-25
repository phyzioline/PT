from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter, BooleanFilter
from django.db import models
from .models import JobPost, JobApplication
from .serializers import (
    JobPostSerializer, 
    JobApplicationSerializer, 
    JobApplicationStatusSerializer
)
from core_data.permissions import IsCompany, IsSpecialist, IsCompanyOrAdmin
from core_data.utils import success_response, error_response


class JobPostFilter(FilterSet):
    """فلاتر للوظائف"""
    location = CharFilter(field_name='location', lookup_expr='icontains')
    search = CharFilter(method='filter_search')
    is_full_time = BooleanFilter(field_name='is_full_time')
    company_id = CharFilter(field_name='company__id')
    
    def filter_search(self, queryset, name, value):
        """بحث في العنوان والوصف"""
        return queryset.filter(
            models.Q(title__icontains=value) | 
            models.Q(description__icontains=value)
        )
    
    class Meta:
        model = JobPost
        fields = ['location', 'is_full_time', 'company_id']


class JobPostViewSet(viewsets.ModelViewSet):
    """
    ViewSet للوظائف
    - GET /api/v1/jobs/ - قائمة الوظائف (للجميع)
    - POST /api/v1/jobs/ - إنشاء وظيفة (للشركات فقط)
    - GET /api/v1/jobs/{id}/ - تفاصيل وظيفة
    - PUT/PATCH /api/v1/jobs/{id}/ - تحديث وظيفة (للمالك فقط)
    - DELETE /api/v1/jobs/{id}/ - حذف وظيفة (للمالك فقط)
    """
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = JobPostFilter
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['posted_at', 'title']
    ordering = ['-posted_at']
    
    def get_permissions(self):
        """تحديد الصلاحيات حسب الإجراء"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsCompany()]
        return [AllowAny()]
    
    def get_queryset(self):
        """تصفية الوظائف حسب المستخدم"""
        queryset = super().get_queryset()
        
        # إذا كان المستخدم شركة، يمكنه رؤية وظائفه فقط في my_jobs
        if self.action == 'my_jobs' and self.request.user.is_authenticated:
            if hasattr(self.request.user, 'userprofile'):
                return queryset.filter(company=self.request.user.userprofile)
        
        return queryset
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated, IsCompany])
    def my_jobs(self, request):
        """الحصول على وظائف الشركة الحالية"""
        jobs = self.get_queryset()
        serializer = self.get_serializer(jobs, many=True)
        return success_response(data=serializer.data, message="تم جلب الوظائف بنجاح")
    
    def perform_create(self, serializer):
        """إنشاء وظيفة جديدة"""
        serializer.save(company=self.request.user.userprofile)


class JobApplicationViewSet(viewsets.ModelViewSet):
    """
    ViewSet لطلبات التقديم
    - GET /api/v1/jobs/applications/ - قائمة الطلبات
    - POST /api/v1/jobs/applications/ - تقديم على وظيفة (للأخصائيين فقط)
    - GET /api/v1/jobs/applications/{id}/ - تفاصيل طلب
    - PATCH /api/v1/jobs/applications/{id}/status/ - تحديث الحالة (للشركة فقط)
    """
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'job', 'applicant']
    search_fields = ['cover_letter', 'job__title']
    ordering_fields = ['applied_at']
    ordering = ['-applied_at']
    
    def get_queryset(self):
        """تصفية الطلبات حسب المستخدم"""
        queryset = super().get_queryset()
        user = self.request.user
        
        if not user.is_authenticated:
            return queryset.none()
        
        # إذا كان أخصائي، يرى طلباته فقط
        if hasattr(user, 'userprofile') and user.userprofile.role == 'specialist':
            return queryset.filter(applicant=user.userprofile)
        
        # إذا كان شركة، يرى طلبات وظائفه فقط
        elif hasattr(user, 'userprofile') and user.userprofile.role == 'company':
            return queryset.filter(job__company=user.userprofile)
        
        # المسؤولون يرون كل شيء
        elif user.is_staff:
            return queryset
        
        return queryset.none()
    
    def get_permissions(self):
        """تحديد الصلاحيات"""
        if self.action == 'create':
            return [IsAuthenticated(), IsSpecialist()]
        elif self.action == 'update_status':
            return [IsAuthenticated(), IsCompanyOrAdmin()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        """إنشاء طلب تقديم"""
        job_id = serializer.validated_data.get('job_id')
        job = JobPost.objects.get(id=job_id)
        
        # التحقق من عدم التقديم مرتين
        if JobApplication.objects.filter(
            job=job, 
            applicant=self.request.user.userprofile
        ).exists():
            from rest_framework.exceptions import ValidationError
            raise ValidationError("لقد تقدمت لهذه الوظيفة مسبقاً")
        
        serializer.save(applicant=self.request.user.userprofile, job=job)
    
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated, IsCompanyOrAdmin])
    def update_status(self, request, pk=None):
        """تحديث حالة طلب التقديم"""
        application = self.get_object()
        
        # التحقق من أن المستخدم هو صاحب الوظيفة
        if not request.user.is_staff:
            if application.job.company.user != request.user:
                return error_response(
                    message="ليس لديك صلاحية لتحديث حالة هذا الطلب",
                    status_code=status.HTTP_403_FORBIDDEN
                )
        
        serializer = JobApplicationStatusSerializer(application, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                data=JobApplicationSerializer(application).data,
                message="تم تحديث الحالة بنجاح"
            )
        return error_response(errors=serializer.errors)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_applications(self, request):
        """الحصول على طلبات المستخدم الحالي"""
        if not hasattr(request.user, 'userprofile'):
            return error_response(message="ملف التعريف غير موجود")
        
        if request.user.userprofile.role == 'specialist':
            applications = self.get_queryset().filter(applicant=request.user.userprofile)
        else:
            return error_response(message="هذا الإجراء للأخصائيين فقط")
        
        serializer = self.get_serializer(applications, many=True)
        return success_response(data=serializer.data, message="تم جلب الطلبات بنجاح")
