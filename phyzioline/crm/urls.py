from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, MessageViewSet, CRMCampaignViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'campaigns', CRMCampaignViewSet, basename='crmcampaign')

app_name = 'crm'

urlpatterns = [
    path('', include(router.urls)),
]

