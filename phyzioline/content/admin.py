from django.contrib import admin
from .models import EquivalenceRequirement, ExploreDataPoint
from .models import Ad

@admin.register(EquivalenceRequirement)
class EquivalenceRequirementAdmin(admin.ModelAdmin):
    list_display = ('country_name_ar', 'country_code', 'get_official_requirements_summary', 'mandatory_exams')
    search_fields = ('country_name_ar', 'official_requirements')
    list_filter = ('country_name_ar',)

    def get_official_requirements_summary(self, obj):
        return obj.official_requirements[:50] + '...' if len(obj.official_requirements) > 50 else obj.official_requirements
    get_official_requirements_summary.short_description = 'Official Req Summary'


@admin.register(ExploreDataPoint)
class ExploreDataPointAdmin(admin.ModelAdmin):
    list_display = ('country', 'data_type', 'value', 'year')
    list_filter = ('data_type', 'year', 'country')
    search_fields = ('country',)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'sponsor', 'price', 'created_at')
    search_fields = ('title', 'sponsor')
    list_filter = ('sponsor',)
