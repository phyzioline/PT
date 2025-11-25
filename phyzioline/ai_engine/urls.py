from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, TreatmentPlanViewSet, SearchViewSet

router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet, basename='exercise')
router.register(r'treatment-plans', TreatmentPlanViewSet, basename='treatmentplan')
router.register(r'search', SearchViewSet, basename='search')

app_name = 'ai_engine'

urlpatterns = [
    path('', include(router.urls)),
]

