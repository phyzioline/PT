from rest_framework import serializers
from .models import EquivalenceRequirement, ExploreDataPoint
from .models import Ad

class EquivalenceRequirementSerializer(serializers.ModelSerializer):
    """Serializer لمتطلبات المعادلة."""
    
    class Meta:
        model = EquivalenceRequirement
        fields = ['id', 'country_name_ar', 'country_code', 'official_requirements', 'theoretical_practical_hours', 'mandatory_exams', 'general_notes']


class ExploreDataPointSerializer(serializers.ModelSerializer):
    """Serializer لنقاط بيانات الاستكشاف."""
    class Meta:
        model = ExploreDataPoint
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'sponsor', 'summary', 'price', 'created_at']
