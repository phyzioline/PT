from django.contrib import admin
from .models import TreatmentPlan, Exercise, SearchLog


@admin.register(TreatmentPlan)
class TreatmentPlanAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'condition', 'is_ai_generated', 'created_at']
    list_filter = ['is_ai_generated', 'created_at']
    search_fields = ['condition', 'diagnosis']


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'difficulty_level', 'duration_minutes']
    list_filter = ['category', 'difficulty_level']
    search_fields = ['name', 'description']


@admin.register(SearchLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'query', 'results_count', 'response_time_ms', 'created_at']
    list_filter = ['created_at']
    search_fields = ['query']

