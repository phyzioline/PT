from rest_framework import serializers
from .models import Contact, Message, CRMCampaign
from accounts.serializers import UserProfileSerializer


class ContactSerializer(serializers.ModelSerializer):
    """Serializer لجهات الاتصال"""
    assigned_to = UserProfileSerializer(read_only=True)
    source_display = serializers.CharField(source='get_source_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    messages_count = serializers.IntegerField(source='messages.count', read_only=True)
    
    class Meta:
        model = Contact
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone',
            'source', 'source_display', 'status', 'status_display',
            'notes', 'assigned_to', 'messages_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MessageSerializer(serializers.ModelSerializer):
    """Serializer للرسائل"""
    contact = ContactSerializer(read_only=True)
    channel_display = serializers.CharField(source='get_channel_display', read_only=True)
    direction_display = serializers.CharField(source='get_direction_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Message
        fields = [
            'id', 'contact', 'channel', 'channel_display', 'direction',
            'direction_display', 'content', 'status', 'status_display',
            'metadata', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class CRMCampaignSerializer(serializers.ModelSerializer):
    """Serializer لحملات CRM"""
    channel_display = serializers.CharField(source='get_channel_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = CRMCampaign
        fields = [
            'id', 'name', 'description', 'channel', 'channel_display',
            'message_template', 'target_audience', 'status', 'status_display',
            'sent_count', 'delivered_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'sent_count', 'delivered_count']

