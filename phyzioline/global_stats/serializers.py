from rest_framework import serializers
from .models import DatasetSnapshot, CountryStat


class CountryStatSerializer(serializers.ModelSerializer):
    therapists_per_100k = serializers.FloatField(read_only=True)

    class Meta:
        model = CountryStat
        fields = [
            "id",
            "dataset",
            "country",
            "continent",
            "population",
            "therapists",
            "schools",
            "centers",
            "avg_salary_usd",
            "therapists_per_100k",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class DatasetSnapshotSerializer(serializers.ModelSerializer):
    country_stats = CountryStatSerializer(many=True, read_only=True)

    class Meta:
        model = DatasetSnapshot
        fields = [
            "id",
            "name",
            "description",
            "source",
            "effective_date",
            "country_stats",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

