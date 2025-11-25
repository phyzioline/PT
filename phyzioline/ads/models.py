from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import UserProfile
from core_data.models import TimeStampedModel


# =================================================================
# 1. الحملات الإعلانية (Campaigns)
# =================================================================
class Campaign(TimeStampedModel):
    """الحملات الإعلانية"""
    advertiser = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='campaigns',
        verbose_name="المعلن"
    )
    
    name = models.CharField(max_length=255, verbose_name="اسم الحملة")
    description = models.TextField(blank=True, verbose_name="الوصف")
    
    budget = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="الميزانية")
    spent = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="المصروف")
    
    start_date = models.DateTimeField(verbose_name="تاريخ البداية")
    end_date = models.DateTimeField(verbose_name="تاريخ النهاية")
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'مسودة'),
            ('active', 'نشط'),
            ('paused', 'متوقف'),
            ('completed', 'مكتمل'),
            ('cancelled', 'ملغي'),
        ],
        default='draft',
        verbose_name="الحالة"
    )
    
    class Meta:
        verbose_name = "حملة إعلانية"
        verbose_name_plural = "الحملات الإعلانية"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


# =================================================================
# 2. الإعلانات (Ads)
# =================================================================
class Ad(TimeStampedModel):
    """الإعلانات"""
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='ads', verbose_name="الحملة")
    
    title = models.CharField(max_length=255, verbose_name="العنوان")
    description = models.TextField(verbose_name="الوصف")
    image = models.ImageField(upload_to='ads/', blank=True, null=True, verbose_name="صورة")
    link_url = models.URLField(blank=True, verbose_name="رابط الإعلان")
    
    ad_type = models.CharField(
        max_length=20,
        choices=[
            ('banner', 'بانر'),
            ('sidebar', 'شريط جانبي'),
            ('feed', 'في Feed'),
            ('popup', 'نافذة منبثقة'),
        ],
        default='banner',
        verbose_name="نوع الإعلان"
    )
    
    target_audience = models.JSONField(default=dict, blank=True, verbose_name="الجمهور المستهدف")
    
    impressions = models.PositiveIntegerField(default=0, verbose_name="عدد المشاهدات")
    clicks = models.PositiveIntegerField(default=0, verbose_name="عدد النقرات")
    ctr = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="نسبة النقر")
    
    is_active = models.BooleanField(default=True, verbose_name="نشط؟")
    
    class Meta:
        verbose_name = "إعلان"
        verbose_name_plural = "الإعلانات"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def calculate_ctr(self):
        """حساب نسبة النقر"""
        if self.impressions > 0:
            self.ctr = (self.clicks / self.impressions) * 100
        return self.ctr


# =================================================================
# 3. التحليلات (Analytics)
# =================================================================
class AdAnalytics(TimeStampedModel):
    """تحليلات الإعلانات"""
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='analytics', verbose_name="الإعلان")
    date = models.DateField(verbose_name="التاريخ")
    
    impressions = models.PositiveIntegerField(default=0, verbose_name="المشاهدات")
    clicks = models.PositiveIntegerField(default=0, verbose_name="النقرات")
    conversions = models.PositiveIntegerField(default=0, verbose_name="التحويلات")
    
    class Meta:
        verbose_name = "تحليل إعلان"
        verbose_name_plural = "تحليلات الإعلانات"
        unique_together = ['ad', 'date']
        ordering = ['-date']
    
    def __str__(self):
        return f"Analytics for {self.ad.title} - {self.date}"

