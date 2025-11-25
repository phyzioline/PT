from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contact, Message, CRMCampaign
from .serializers import ContactSerializer, MessageSerializer, CRMCampaignSerializer
from core_data.utils import success_response


class ContactViewSet(viewsets.ModelViewSet):
    """ViewSet لجهات الاتصال"""
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['source', 'status', 'assigned_to']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على جهات الاتصال"""
        return Contact.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet للرسائل"""
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['contact', 'channel', 'direction', 'status']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على الرسائل"""
        return Message.objects.all()
    
    @action(detail=False, methods=['post'], url_path='whatsapp-webhook')
    def whatsapp_webhook(self, request):
        """Webhook لاستقبال رسائل WhatsApp"""
        # هنا يمكن إضافة منطق استقبال رسائل WhatsApp
        return success_response(message="تم استقبال الرسالة")


class CRMCampaignViewSet(viewsets.ModelViewSet):
    """ViewSet لحملات CRM"""
    serializer_class = CRMCampaignSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['channel', 'status']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على الحملات"""
        return CRMCampaign.objects.all()
    
    @action(detail=True, methods=['post'], url_path='send')
    def send_campaign(self, request, pk=None):
        """إرسال حملة"""
        campaign = self.get_object()
        # هنا يمكن إضافة منطق الإرسال
        return success_response(message="تم إرسال الحملة")

