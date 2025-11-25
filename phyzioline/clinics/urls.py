from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClinicViewSet, PatientViewSet, AppointmentViewSet,
    MedicalNoteViewSet, InvoiceViewSet
)

router = DefaultRouter()
router.register(r'clinics', ClinicViewSet, basename='clinic')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'medical-notes', MedicalNoteViewSet, basename='medicalnote')
router.register(r'invoices', InvoiceViewSet, basename='invoice')

app_name = 'clinics'

urlpatterns = [
    path('', include(router.urls)),
]

