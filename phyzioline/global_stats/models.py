from django.db import models
from core_data.models import TimeStampedModel


class DatasetSnapshot(TimeStampedModel):
    """Represents a snapshot/version of the global stats dataset."""

    name = models.CharField(max_length=120, verbose_name="Dataset Name")
    description = models.TextField(blank=True, verbose_name="Description")
    source = models.CharField(max_length=255, blank=True, verbose_name="Source / Reference")
    effective_date = models.DateField(blank=True, null=True, verbose_name="Effective Date")

    class Meta:
        verbose_name = "Dataset Snapshot"
        verbose_name_plural = "Dataset Snapshots"
        ordering = ["-effective_date", "-created_at"]

    def __str__(self) -> str:
        return self.name


class CountryStat(TimeStampedModel):
    """Stores aggregated statistics per country."""

    dataset = models.ForeignKey(
        DatasetSnapshot, on_delete=models.CASCADE, related_name="country_stats"
    )
    country = models.CharField(max_length=120, verbose_name="Country")
    continent = models.CharField(max_length=60, verbose_name="Continent")
    population = models.BigIntegerField(default=0, verbose_name="Population")
    therapists = models.IntegerField(default=0, verbose_name="Registered Therapists")
    schools = models.IntegerField(default=0, verbose_name="Therapy Schools / Colleges")
    centers = models.IntegerField(default=0, verbose_name="Rehab Centers")
    avg_salary_usd = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Avg Salary (USD)"
    )

    class Meta:
        verbose_name = "Country Stat"
        verbose_name_plural = "Country Stats"
        ordering = ["dataset", "country"]

    @property
    def therapists_per_100k(self) -> float:
        if self.population > 0:
            return round((self.therapists / self.population) * 100_000, 2)
        return 0.0

    def __str__(self) -> str:
        return f"{self.country} ({self.dataset.name})"
