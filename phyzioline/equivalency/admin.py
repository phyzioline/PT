from django.contrib import admin
from .models import Country, EquivalencyRequirement, RequirementDocument


class RequirementDocumentInline(admin.TabularInline):
    model = RequirementDocument
    extra = 0
    fields = ("title", "is_mandatory", "order")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name_en", "code", "region", "continent", "created_at")
    search_fields = ("name_en", "name_local", "code", "region")
    list_filter = ("continent",)


@admin.register(EquivalencyRequirement)
class EquivalencyRequirementAdmin(admin.ModelAdmin):
    list_display = ("country", "summary", "language_requirement", "exam_requirement")
    search_fields = ("country__name_en", "summary", "language_requirement")
    list_filter = ("country__continent",)
    inlines = [RequirementDocumentInline]


@admin.register(RequirementDocument)
class RequirementDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "requirement", "is_mandatory", "order")
    list_filter = ("is_mandatory",)
    search_fields = ("title", "requirement__country__name_en")
