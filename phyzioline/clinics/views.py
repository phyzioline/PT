from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Clinic, Patient, Appointment, MedicalNote, Invoice
from .serializers import (
    ClinicSerializer, PatientSerializer, AppointmentSerializer,
    MedicalNoteSerializer, InvoiceSerializer
)
from core_data.permissions import IsCompany, IsDoctor
from core_data.utils import success_response


class ClinicViewSet(viewsets.ModelViewSet):
    """ViewSet للعيادات"""
    serializer_class = ClinicSerializer
    permission_classes = [IsAuthenticated, IsCompany]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['city', 'subscription_tier', 'is_active']
    search_fields = ['name', 'description', 'address']
    ordering_fields = ['created_at', 'name']
    ordering = ['-created_at']
    lookup_field = 'slug'
    
    def get_queryset(self):
        """الحصول على عيادات الشركة الحالية"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            return Clinic.objects.filter(company=self.request.user.userprofile, is_deleted=False)
        return Clinic.objects.none()
    
    def perform_create(self, serializer):
        """إنشاء عيادة جديدة"""
        serializer.save(company=self.request.user.userprofile)


class PatientViewSet(viewsets.ModelViewSet):
    """ViewSet للمرضى"""
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['clinic', 'gender']
    search_fields = ['first_name', 'last_name', 'phone', 'email']
    
    def get_queryset(self):
        """الحصول على مرضى العيادات التابعة للشركة"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            if self.request.user.userprofile.role == 'company':
                clinics = Clinic.objects.filter(company=self.request.user.userprofile)
                return Patient.objects.filter(clinic__in=clinics)
            elif self.request.user.userprofile.role == 'doctor':
                return Patient.objects.filter(clinic__appointments__doctor=self.request.user.userprofile).distinct()
        return Patient.objects.none()


class AppointmentViewSet(viewsets.ModelViewSet):
    """ViewSet للمواعيد"""
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['clinic', 'patient', 'doctor', 'status']
    ordering_fields = ['appointment_date']
    ordering = ['appointment_date']
    
    def get_queryset(self):
        """الحصول على المواعيد"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            if self.request.user.userprofile.role == 'company':
                clinics = Clinic.objects.filter(company=self.request.user.userprofile)
                return Appointment.objects.filter(clinic__in=clinics)
            elif self.request.user.userprofile.role == 'doctor':
                return Appointment.objects.filter(doctor=self.request.user.userprofile)
        return Appointment.objects.none()
    
    def perform_create(self, serializer):
        """إنشاء موعد جديد"""
        if self.request.user.userprofile.role == 'doctor':
            serializer.save(doctor=self.request.user.userprofile)
        else:
            serializer.save()


class MedicalNoteViewSet(viewsets.ModelViewSet):
    """ViewSet للملاحظات الطبية"""
    serializer_class = MedicalNoteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['appointment', 'doctor']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على الملاحظات"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            if self.request.user.userprofile.role == 'doctor':
                return MedicalNote.objects.filter(doctor=self.request.user.userprofile)
            elif self.request.user.userprofile.role == 'company':
                clinics = Clinic.objects.filter(company=self.request.user.userprofile)
                return MedicalNote.objects.filter(appointment__clinic__in=clinics)
        return MedicalNote.objects.none()
    
    def perform_create(self, serializer):
        """إنشاء ملاحظة طبية"""
        serializer.save(doctor=self.request.user.userprofile)


class InvoiceViewSet(viewsets.ModelViewSet):
    """ViewSet للفواتير"""
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['clinic', 'patient', 'status']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على الفواتير"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            if self.request.user.userprofile.role == 'company':
                clinics = Clinic.objects.filter(company=self.request.user.userprofile)
                return Invoice.objects.filter(clinic__in=clinics)
        return Invoice.objects.none()

