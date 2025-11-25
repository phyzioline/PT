from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, AdViewSet, AdAnalyticsViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')
router.register(r'ads', AdViewSet, basename='ad')
router.register(r'analytics', AdAnalyticsViewSet, basename='analytics')

app_name = 'ads'

urlpatterns = [
    path('', include(router.urls)),
]

