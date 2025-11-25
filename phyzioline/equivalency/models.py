from django.db import models
from core_data.models import TimeStampedModel


class Country(TimeStampedModel):
    """Represents a country with equivalency requirements."""

    code = models.CharField(max_length=5, unique=True, verbose_name="Country Code")
    name_en = models.CharField(max_length=120, verbose_name="English Name")
    name_local = models.CharField(
        max_length=120, blank=True, verbose_name="Local / Arabic Name"
    )
    region = models.CharField(max_length=120, blank=True, verbose_name="Region")
    continent = models.CharField(
        max_length=60,
        choices=[
            ("africa", "Africa"),
            ("asia", "Asia"),
            ("europe", "Europe"),
            ("americas", "Americas"),
            ("oceania", "Oceania"),
            ("global", "Global"),
        ],
        default="asia",
        verbose_name="Continent",
    )

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name_en"]

    def __str__(self) -> str:
        return f"{self.name_en} ({self.code})"


class EquivalencyRequirement(TimeStampedModel):
    """Detailed requirements for practising physiotherapy in a country."""

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="requirements"
    )
    summary = models.TextField(verbose_name="Summary")
    study_hours = models.CharField(
        max_length=255, blank=True, verbose_name="Study / Bridging Hours"
    )
    accredited_hours = models.CharField(
        max_length=255, blank=True, verbose_name="Accredited Hours"
    )
    language_requirement = models.CharField(
        max_length=255, blank=True, verbose_name="Language Requirement"
    )
    exam_requirement = models.CharField(
        max_length=255, blank=True, verbose_name="Exam / Assessment"
    )
    notes = models.TextField(blank=True, verbose_name="Additional Notes")

    class Meta:
        verbose_name = "Equivalency Requirement"
        verbose_name_plural = "Equivalency Requirements"
        ordering = ["country__name_en"]

    def __str__(self) -> str:
        return f"{self.country.name_en} Requirement"


class RequirementDocument(TimeStampedModel):
    """Supporting document checklist for a requirement."""

    requirement = models.ForeignKey(
        EquivalencyRequirement, on_delete=models.CASCADE, related_name="documents"
    )
    title = models.CharField(max_length=255, verbose_name="Document Title")
    description = models.TextField(blank=True, verbose_name="Description / Details")
    is_mandatory = models.BooleanField(default=True, verbose_name="Is Mandatory?")
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Requirement Document"
        verbose_name_plural = "Requirement Documents"
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return f"{self.title} ({'Mandatory' if self.is_mandatory else 'Optional'})"
