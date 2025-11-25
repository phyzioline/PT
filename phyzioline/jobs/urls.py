from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPostViewSet, JobApplicationViewSet

router = DefaultRouter()
router.register(r'posts', JobPostViewSet, basename='jobpost')
router.register(r'applications', JobApplicationViewSet, basename='jobapplication')

app_name = 'jobs'

urlpatterns = [
    path('', include(router.urls)),
]

