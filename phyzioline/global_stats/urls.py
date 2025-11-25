from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DatasetSnapshotViewSet, CountryStatViewSet

router = DefaultRouter()
router.register(r"snapshots", DatasetSnapshotViewSet, basename="stats-snapshot")
router.register(r"countries", CountryStatViewSet, basename="stats-country")

app_name = "global_stats"

urlpatterns = [
    path("", include(router.urls)),
]

