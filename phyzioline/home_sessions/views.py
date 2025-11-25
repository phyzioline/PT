from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import SpecialistAvailability, Session, SessionReview
from .serializers import (
    SpecialistAvailabilitySerializer, SessionSerializer, SessionReviewSerializer
)
from core_data.permissions import IsSpecialist
from core_data.utils import success_response


class SpecialistAvailabilityViewSet(viewsets.ModelViewSet):
    """ViewSet لتوفر الأخصائيين"""
    serializer_class = SpecialistAvailabilitySerializer
    permission_classes = [IsAuthenticated, IsSpecialist]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date', 'is_available']
    ordering_fields = ['date', 'start_time']
    ordering = ['date', 'start_time']
    
    def get_queryset(self):
        """الحصول على توفر الأخصائي الحالي"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            return SpecialistAvailability.objects.filter(specialist=self.request.user.userprofile)
        return SpecialistAvailability.objects.none()
    
    def perform_create(self, serializer):
        """إنشاء توفر جديد"""
        serializer.save(specialist=self.request.user.userprofile)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def nearby(self, request):
        """البحث عن أخصائيين قريبين"""
        lat = float(request.query_params.get('latitude', 0))
        lng = float(request.query_params.get('longitude', 0))
        radius = int(request.query_params.get('radius', 10))
        
        # بحث بسيط (يمكن تحسينه باستخدام geolocation libraries)
        availabilities = SpecialistAvailability.objects.filter(
            is_available=True,
            location_latitude__gte=lat - (radius / 111),  # تقريب بسيط
            location_latitude__lte=lat + (radius / 111),
            location_longitude__gte=lng - (radius / 111),
            location_longitude__lte=lng + (radius / 111),
        )
        
        serializer = self.get_serializer(availabilities, many=True)
        return success_response(data=serializer.data)


class SessionViewSet(viewsets.ModelViewSet):
    """ViewSet للجلسات"""
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['specialist', 'patient', 'status']
    ordering_fields = ['session_date']
    ordering = ['session_date']
    
    def get_queryset(self):
        """الحصول على الجلسات"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            user_profile = self.request.user.userprofile
            return Session.objects.filter(
                Q(specialist=user_profile) | Q(patient=user_profile)
            )
        return Session.objects.none()
    
    def perform_create(self, serializer):
        """إنشاء جلسة جديدة"""
        if self.request.user.userprofile.role == 'patient':
            serializer.save(patient=self.request.user.userprofile)


class SessionReviewViewSet(viewsets.ModelViewSet):
    """ViewSet لتقييمات الجلسات"""
    serializer_class = SessionReviewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['session', 'rating']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على التقييمات"""
        return SessionReview.objects.all()
    
    def perform_create(self, serializer):
        """إنشاء تقييم جديد"""
        serializer.save(reviewer=self.request.user.userprofile)

