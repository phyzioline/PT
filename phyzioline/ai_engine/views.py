from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models
import time
from .models import TreatmentPlan, Exercise, SearchLog
from .serializers import TreatmentPlanSerializer, ExerciseSerializer, SearchLogSerializer
from core_data.utils import success_response, error_response


class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet للتمارين"""
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'difficulty_level']
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    ordering = ['name']


class TreatmentPlanViewSet(viewsets.ModelViewSet):
    """ViewSet لخطط العلاج"""
    serializer_class = TreatmentPlanSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['patient', 'doctor', 'condition']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على خطط العلاج"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            user_profile = self.request.user.userprofile
            if user_profile.role == 'patient':
                return TreatmentPlan.objects.filter(patient=user_profile)
            elif user_profile.role == 'doctor':
                return TreatmentPlan.objects.filter(doctor=user_profile)
        return TreatmentPlan.objects.none()
    
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def generate(self, request):
        """إنشاء خطة علاج بالذكاء الاصطناعي"""
        condition = request.data.get('condition')
        diagnosis = request.data.get('diagnosis', '')
        
        if not condition:
            return error_response(message="condition مطلوب")
        
        # هنا يمكن إضافة منطق AI حقيقي (OpenAI, Claude, etc.)
        # حالياً سنعيد خطة بسيطة
        treatment_plan = TreatmentPlan.objects.create(
            patient=request.user.userprofile,
            condition=condition,
            diagnosis=diagnosis,
            treatment_plan="خطة علاج مخصصة بناءً على الحالة...",
            exercises=[],
            is_ai_generated=True
        )
        
        serializer = self.get_serializer(treatment_plan)
        return success_response(data=serializer.data, message="تم إنشاء خطة العلاج")


class SearchViewSet(viewsets.ViewSet):
    """ViewSet للبحث بالذكاء الاصطناعي"""
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def search(self, request):
        """بحث ذكي"""
        query = request.data.get('query', '')
        if not query:
            return error_response(message="query مطلوب")
        
        start_time = time.time()
        
        # بحث بسيط في التمارين (يمكن تحسينه بـ NLP)
        exercises = Exercise.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query) |
            models.Q(instructions__icontains=query)
        )[:10]
        
        response_time = int((time.time() - start_time) * 1000)
        
        # حفظ سجل البحث
        user_profile = None
        if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
            user_profile = request.user.userprofile
        
        SearchLog.objects.create(
            user=user_profile,
            query=query,
            results_count=exercises.count(),
            response_time_ms=response_time
        )
        
        serializer = ExerciseSerializer(exercises, many=True)
        return success_response(data=serializer.data, message="تم البحث بنجاح")

