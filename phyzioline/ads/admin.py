from django.contrib import admin
from .models import Campaign, Ad, AdAnalytics


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'advertiser', 'budget', 'spent', 'status', 'start_date']
    list_filter = ['status', 'start_date']
    search_fields = ['name', 'description']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'campaign', 'ad_type', 'impressions', 'clicks', 'ctr', 'is_active']
    list_filter = ['ad_type', 'is_active', 'created_at']
    search_fields = ['title', 'description']


@admin.register(AdAnalytics)
class AdAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['ad', 'date', 'impressions', 'clicks', 'conversions']
    list_filter = ['date']
    search_fields = ['ad__title']

