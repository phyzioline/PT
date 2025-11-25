from rest_framework import serializers
from .models import SpecialistAvailability, Session, SessionReview
from accounts.serializers import UserProfileSerializer


class SpecialistAvailabilitySerializer(serializers.ModelSerializer):
    """Serializer لتوفر الأخصائيين"""
    specialist = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = SpecialistAvailability
        fields = [
            'id', 'specialist', 'date', 'start_time', 'end_time',
            'location_latitude', 'location_longitude', 'location_address',
            'service_radius_km', 'hourly_rate', 'is_available', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class SessionSerializer(serializers.ModelSerializer):
    """Serializer للجلسات"""
    specialist = UserProfileSerializer(read_only=True)
    patient = UserProfileSerializer(read_only=True)
    availability = SpecialistAvailabilitySerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Session
        fields = [
            'id', 'specialist', 'patient', 'availability', 'session_date',
            'duration_hours', 'location_latitude', 'location_longitude',
            'location_address', 'hourly_rate', 'total_amount', 'status',
            'status_display', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class SessionReviewSerializer(serializers.ModelSerializer):
    """Serializer لتقييمات الجلسات"""
    session = SessionSerializer(read_only=True)
    reviewer = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = SessionReview
        fields = ['id', 'session', 'reviewer', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'reviewer', 'created_at']

