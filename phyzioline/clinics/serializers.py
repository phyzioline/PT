from rest_framework import serializers
from .models import Clinic, Patient, Appointment, MedicalNote, Invoice
from accounts.serializers import UserProfileSerializer


class ClinicSerializer(serializers.ModelSerializer):
    """Serializer للعيادات"""
    company = UserProfileSerializer(read_only=True)
    patients_count = serializers.IntegerField(source='patients.count', read_only=True)
    appointments_count = serializers.IntegerField(source='appointments.count', read_only=True)
    
    class Meta:
        model = Clinic
        fields = [
            'id', 'company', 'name', 'slug', 'description', 'address',
            'city', 'country', 'phone', 'email', 'subscription_tier',
            'subscription_start', 'subscription_end', 'is_active',
            'patients_count', 'appointments_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'company']


class PatientSerializer(serializers.ModelSerializer):
    """Serializer للمرضى"""
    clinic = ClinicSerializer(read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id', 'clinic', 'first_name', 'last_name', 'phone', 'email',
            'date_of_birth', 'gender', 'address', 'medical_history',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AppointmentSerializer(serializers.ModelSerializer):
    """Serializer للمواعيد"""
    clinic = ClinicSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    doctor = UserProfileSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Appointment
        fields = [
            'id', 'clinic', 'patient', 'doctor', 'appointment_date',
            'duration_minutes', 'status', 'status_display', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MedicalNoteSerializer(serializers.ModelSerializer):
    """Serializer للملاحظات الطبية"""
    appointment = AppointmentSerializer(read_only=True)
    doctor = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = MedicalNote
        fields = [
            'id', 'appointment', 'doctor', 'diagnosis', 'treatment_plan',
            'prescription', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class InvoiceSerializer(serializers.ModelSerializer):
    """Serializer للفواتير"""
    clinic = ClinicSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    appointment = AppointmentSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Invoice
        fields = [
            'id', 'clinic', 'patient', 'appointment', 'invoice_number',
            'amount', 'tax', 'total', 'status', 'status_display',
            'paid_at', 'payment_method', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'invoice_number', 'created_at', 'updated_at']

