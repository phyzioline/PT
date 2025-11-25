from rest_framework import serializers
from .models import Campaign, Ad, AdAnalytics
from accounts.serializers import UserProfileSerializer


class CampaignSerializer(serializers.ModelSerializer):
    """Serializer للحملات"""
    advertiser = UserProfileSerializer(read_only=True)
    ads_count = serializers.IntegerField(source='ads.count', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Campaign
        fields = [
            'id', 'advertiser', 'name', 'description', 'budget', 'spent',
            'start_date', 'end_date', 'status', 'status_display', 'ads_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'advertiser', 'spent']


class AdSerializer(serializers.ModelSerializer):
    """Serializer للإعلانات"""
    campaign = CampaignSerializer(read_only=True)
    ad_type_display = serializers.CharField(source='get_ad_type_display', read_only=True)
    
    class Meta:
        model = Ad
        fields = [
            'id', 'campaign', 'title', 'description', 'image', 'link_url',
            'ad_type', 'ad_type_display', 'target_audience', 'impressions',
            'clicks', 'ctr', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'impressions', 'clicks', 'ctr']


class AdAnalyticsSerializer(serializers.ModelSerializer):
    """Serializer للتحليلات"""
    ad = AdSerializer(read_only=True)
    
    class Meta:
        model = AdAnalytics
        fields = ['id', 'ad', 'date', 'impressions', 'clicks', 'conversions', 'created_at']
        read_only_fields = ['id', 'created_at']

