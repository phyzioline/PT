from django.db import models
from django.utils.translation import gettext_lazy as _

# موديل متطلبات المعادلة (Equivalence Requirements)
class EquivalenceRequirement(models.Model):
    """يخزن متطلبات المعادلة والعمل الخاصة بدولة معينة."""
    
    country_name_ar = models.CharField(
        _("Country Name (Arabic)"),
        max_length=100,
        unique=True,
        help_text=_("The full name of the country in Arabic (e.g., المملكة العربية السعودية).")
    )
    country_code = models.CharField(
        _("Country Code (ISO 2)"),
        max_length=2,
        unique=True,
        help_text=_("The two-letter ISO country code (e.g., SA for Saudi Arabia, US for USA).")
    )
    
    official_requirements = models.TextField(
        _("Official Requirements"),
        help_text=_("Detailed list of formal papers and registrations.")
    )
    
    theoretical_practical_hours = models.TextField(
        _("Theoretical and Practical Hours"),
        help_text=_("Details about required academic and practical hours.")
    )
    
    mandatory_exams = models.TextField(
        _("Mandatory Exams"),
        help_text=_("Information about licensing exams (e.g., Prometric, MOH).")
    )
    
    general_notes = models.TextField(
        _("General Notes"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Equivalence Requirement")
        verbose_name_plural = _("Equivalence Requirements")
        ordering = ['country_name_ar']
        indexes = [models.Index(fields=['country_code']), models.Index(fields=['country_name_ar'])]
        
    def __str__(self):
        return f"متطلبات المعادلة - {self.country_name_ar}"


# موديل بيانات الاستكشاف (Explore Data) - لا يحتاج إلى تعديل
class ExploreDataPoint(models.Model):
    """يخزن نقاط البيانات لصفحة الاستكشاف (Explore)."""

    DATA_TYPE_CHOICES = [
        ('THERAPISTS', 'Registered Therapists'),
        ('POPULATION', 'Relevant Population Size'),
        ('SCHOOLS', 'Schools/Colleges'),
        ('REHAB_CENTERS', 'Rehab Centers'),
    ]

    country = models.CharField(_("Country Name"), max_length=100)
    data_type = models.CharField(
        _("Data Type"),
        max_length=50,
        choices=DATA_TYPE_CHOICES
    )
    value = models.IntegerField(_("Data Value"))
    year = models.IntegerField(_("Year of Data"), default=2024)

    class Meta:
        verbose_name = _("Explore Data Point")
        verbose_name_plural = _("Explore Data Points")
        unique_together = ('country', 'data_type', 'year')
        ordering = ['-year', 'country', 'data_type']
        indexes = [models.Index(fields=['data_type']), models.Index(fields=['country'])]
        
    def __str__(self):
        return f"{self.country} - {self.get_data_type_display()}: {self.value}"


class Ad(models.Model):
    """Simple persistent Ad model for the `ads` module demo."""
    title = models.CharField(max_length=200)
    sponsor = models.CharField(max_length=120, blank=True)
    summary = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.sponsor})"
