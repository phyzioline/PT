from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Campaign, Ad, AdAnalytics
from .serializers import CampaignSerializer, AdSerializer, AdAnalyticsSerializer
from core_data.utils import success_response


class CampaignViewSet(viewsets.ModelViewSet):
    """ViewSet للحملات"""
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على حملات المعلن الحالي"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            return Campaign.objects.filter(advertiser=self.request.user.userprofile)
        return Campaign.objects.none()
    
    def perform_create(self, serializer):
        """إنشاء حملة جديدة"""
        serializer.save(advertiser=self.request.user.userprofile)


class AdViewSet(viewsets.ModelViewSet):
    """ViewSet للإعلانات"""
    queryset = Ad.objects.filter(is_active=True)
    serializer_class = AdSerializer
    permission_classes = [AllowAny]  # للإعلانات العامة
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['campaign', 'ad_type', 'is_active']
    ordering_fields = ['created_at', 'impressions', 'clicks']
    ordering = ['-created_at']
    
    @action(detail=True, methods=['post'], permission_classes=[AllowAny])
    def track_click(self, request, pk=None):
        """تتبع النقرات"""
        ad = self.get_object()
        ad.clicks += 1
        ad.calculate_ctr()
        ad.save()
        return success_response(message="تم تتبع النقرة")
    
    @action(detail=True, methods=['post'], permission_classes=[AllowAny])
    def track_impression(self, request, pk=None):
        """تتبع المشاهدات"""
        ad = self.get_object()
        ad.impressions += 1
        ad.calculate_ctr()
        ad.save()
        return success_response(message="تم تتبع المشاهدة")


class AdAnalyticsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet للتحليلات"""
    serializer_class = AdAnalyticsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['ad', 'date']
    ordering_fields = ['date']
    ordering = ['-date']
    
    def get_queryset(self):
        """الحصول على تحليلات إعلانات المعلن"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            campaigns = Campaign.objects.filter(advertiser=self.request.user.userprofile)
            ads = Ad.objects.filter(campaign__in=campaigns)
            return AdAnalytics.objects.filter(ad__in=ads)
        return AdAnalytics.objects.none()

