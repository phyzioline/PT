from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, EquivalencyRequirementViewSet

router = DefaultRouter()
router.register(r"countries", CountryViewSet, basename="equivalency-country")
router.register(
    r"requirements", EquivalencyRequirementViewSet, basename="equivalency-requirement"
)

app_name = "equivalency"

urlpatterns = [
    path("", include(router.urls)),
]

