from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Country, EquivalencyRequirement
from .serializers import CountrySerializer, EquivalencyRequirementSerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """Public API for listing/viewing countries and their requirements."""

    queryset = Country.objects.all().prefetch_related("requirements__documents")
    serializer_class = CountrySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name_en", "name_local", "code", "region"]
    filterset_fields = ["continent", "region"]
    ordering = ["name_en"]


class EquivalencyRequirementViewSet(viewsets.ReadOnlyModelViewSet):
    """Detailed requirements per country (read only)."""

    queryset = EquivalencyRequirement.objects.select_related("country").prefetch_related(
        "documents"
    )
    serializer_class = EquivalencyRequirementSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["country__name_en", "summary", "language_requirement"]
    filterset_fields = ["country__continent", "country__code"]
