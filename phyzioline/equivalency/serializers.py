from rest_framework import serializers
from .models import Country, EquivalencyRequirement, RequirementDocument


class RequirementDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementDocument
        fields = [
            "id",
            "title",
            "description",
            "is_mandatory",
            "order",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class EquivalencyRequirementSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    documents = RequirementDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = EquivalencyRequirement
        fields = [
            "id",
            "country",
            "summary",
            "study_hours",
            "accredited_hours",
            "language_requirement",
            "exam_requirement",
            "notes",
            "documents",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class CountrySerializer(serializers.ModelSerializer):
    requirements = EquivalencyRequirementSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = [
            "id",
            "code",
            "name_en",
            "name_local",
            "region",
            "continent",
            "requirements",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

