from django.contrib import admin
from .models import SpecialistAvailability, Session, SessionReview


@admin.register(SpecialistAvailability)
class SpecialistAvailabilityAdmin(admin.ModelAdmin):
    list_display = ['specialist', 'date', 'start_time', 'end_time', 'is_available']
    list_filter = ['date', 'is_available']
    search_fields = ['specialist__user__username']


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'specialist', 'session_date', 'status', 'total_amount']
    list_filter = ['status', 'session_date']
    search_fields = ['patient__user__username', 'specialist__user__username']


@admin.register(SessionReview)
class SessionReviewAdmin(admin.ModelAdmin):
    list_display = ['session', 'reviewer', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']

