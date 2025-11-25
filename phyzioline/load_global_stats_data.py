"""
Load sample global physiotherapy statistics inspired by `m.html explore` file.

Usage:
    python load_global_stats_data.py
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phyzioline_core.settings")
django.setup()

from global_stats.models import DatasetSnapshot, CountryStat

COUNTRY_STATS = [
    {
        "country": "USA",
        "continent": "North America",
        "population": 331_893_745,
        "therapists": 231_000,
        "schools": 250,
        "centers": 19_500,
    },
    {
        "country": "Canada",
        "continent": "North America",
        "population": 38_005_238,
        "therapists": 27_000,
        "schools": 17,
        "centers": 2_200,
    },
    {
        "country": "Germany",
        "continent": "Europe",
        "population": 83_900_473,
        "therapists": 205_000,
        "schools": 200,
        "centers": 8_500,
    },
    {
        "country": "Egypt",
        "continent": "Africa",
        "population": 104_258_327,
        "therapists": 18_000,
        "schools": 25,
        "centers": 800,
    },
    {
        "country": "Saudi Arabia",
        "continent": "Asia",
        "population": 34_813_871,
        "therapists": 7_500,
        "schools": 18,
        "centers": 600,
    },
    {
        "country": "India",
        "continent": "Asia",
        "population": 1_393_409_038,
        "therapists": 65_000,
        "schools": 400,
        "centers": 7_500,
    },
]


def main():
    dataset, _ = DatasetSnapshot.objects.get_or_create(
        name="Global Physiotherapy Landscape",
        defaults={
            "description": "Aggregated statistics inspired by research dashboard.",
            "source": "Phyzioline Research",
        },
    )

    for stat in COUNTRY_STATS:
        CountryStat.objects.update_or_create(
            dataset=dataset,
            country=stat["country"],
            defaults=stat,
        )

    print("✅ Global stats dataset populated.")


if __name__ == "__main__":
    main()

