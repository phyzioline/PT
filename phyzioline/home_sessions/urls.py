from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SpecialistAvailabilityViewSet, SessionViewSet, SessionReviewViewSet
)

router = DefaultRouter()
router.register(r'availabilities', SpecialistAvailabilityViewSet, basename='availability')
router.register(r'sessions', SessionViewSet, basename='session')
router.register(r'reviews', SessionReviewViewSet, basename='sessionreview')

app_name = 'sessions'

urlpatterns = [
    path('', include(router.urls)),
]

