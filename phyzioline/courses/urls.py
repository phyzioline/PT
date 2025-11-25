from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, EnrollmentViewSet, CourseReviewViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'reviews', CourseReviewViewSet, basename='coursereview')

app_name = 'courses'

urlpatterns = [
    path('', include(router.urls)),
]

