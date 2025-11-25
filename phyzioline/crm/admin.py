from django.contrib import admin
from .models import Contact, Message, CRMCampaign


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'source', 'status', 'assigned_to']
    list_filter = ['source', 'status', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['contact', 'channel', 'direction', 'status', 'created_at']
    list_filter = ['channel', 'direction', 'status', 'created_at']
    search_fields = ['contact__first_name', 'content']


@admin.register(CRMCampaign)
class CRMCampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'channel', 'status', 'sent_count', 'delivered_count', 'created_at']
    list_filter = ['channel', 'status', 'created_at']
    search_fields = ['name', 'description']

