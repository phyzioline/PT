from django.contrib import admin
from .models import DatasetSnapshot, CountryStat


class CountryStatInline(admin.TabularInline):
    model = CountryStat
    extra = 0
    fields = ("country", "continent", "population", "therapists", "schools", "centers")


@admin.register(DatasetSnapshot)
class DatasetSnapshotAdmin(admin.ModelAdmin):
    list_display = ("name", "effective_date", "source", "created_at")
    search_fields = ("name", "source")
    inlines = [CountryStatInline]


@admin.register(CountryStat)
class CountryStatAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "continent",
        "population",
        "therapists",
        "therapists_per_100k",
        "dataset",
    )
    list_filter = ("continent", "dataset")
    search_fields = ("country",)
