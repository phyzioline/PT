from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import DatasetSnapshot, CountryStat
from .serializers import DatasetSnapshotSerializer, CountryStatSerializer


class DatasetSnapshotViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DatasetSnapshot.objects.all().prefetch_related("country_stats")
    serializer_class = DatasetSnapshotSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name", "description", "source"]
    filterset_fields = ["effective_date"]


class CountryStatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CountryStat.objects.select_related("dataset")
    serializer_class = CountryStatSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ["country", "continent"]
    filterset_fields = ["continent", "dataset", "country"]
    ordering_fields = ["therapists", "population", "therapists_per_100k"]
