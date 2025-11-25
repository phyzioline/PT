from rest_framework import serializers
from .models import TreatmentPlan, Exercise, SearchLog
from accounts.serializers import UserProfileSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer للتمارين"""
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    difficulty_level_display = serializers.CharField(source='get_difficulty_level_display', read_only=True)
    
    class Meta:
        model = Exercise
        fields = [
            'id', 'name', 'description', 'instructions', 'image', 'video_url',
            'category', 'category_display', 'difficulty_level', 'difficulty_level_display',
            'duration_minutes', 'repetitions'
        ]
        read_only_fields = ['id']


class TreatmentPlanSerializer(serializers.ModelSerializer):
    """Serializer لخطط العلاج"""
    patient = UserProfileSerializer(read_only=True)
    doctor = UserProfileSerializer(read_only=True)
    exercises = ExerciseSerializer(many=True, read_only=True)
    
    class Meta:
        model = TreatmentPlan
        fields = [
            'id', 'patient', 'doctor', 'condition', 'diagnosis',
            'treatment_plan', 'exercises', 'duration_weeks', 'is_ai_generated',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class SearchLogSerializer(serializers.ModelSerializer):
    """Serializer لسجلات البحث"""
    user = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = SearchLog
        fields = ['id', 'user', 'query', 'results_count', 'response_time_ms', 'created_at']
        read_only_fields = ['id', 'created_at']

