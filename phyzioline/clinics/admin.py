from django.contrib import admin
from .models import Clinic, Patient, Appointment, MedicalNote, Invoice


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'city', 'subscription_tier', 'is_active']
    list_filter = ['subscription_tier', 'is_active', 'city']
    search_fields = ['name', 'address']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'clinic', 'phone', 'created_at']
    list_filter = ['clinic', 'gender', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone', 'email']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'appointment_date', 'status', 'clinic']
    list_filter = ['status', 'appointment_date', 'clinic']
    search_fields = ['patient__first_name', 'patient__last_name']


@admin.register(MedicalNote)
class MedicalNoteAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'doctor', 'created_at']
    list_filter = ['created_at']
    search_fields = ['appointment__patient__first_name']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'patient', 'clinic', 'total', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['invoice_number', 'patient__first_name']

