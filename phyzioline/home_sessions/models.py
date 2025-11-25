from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import UserProfile
from core_data.models import TimeStampedModel


# =================================================================
# 1. توفر الأخصائيين (Specialist Availability)
# =================================================================
class SpecialistAvailability(TimeStampedModel):
    """توفر الأخصائيين للجلسات المنزلية"""
    specialist = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='availabilities',
        verbose_name="الأخصائي",
        limit_choices_to={'role': 'specialist'}
    )
    
    date = models.DateField(verbose_name="التاريخ")
    start_time = models.TimeField(verbose_name="وقت البداية")
    end_time = models.TimeField(verbose_name="وقت النهاية")
    
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="خط العرض")
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="خط الطول")
    location_address = models.TextField(verbose_name="العنوان")
    service_radius_km = models.PositiveIntegerField(default=10, verbose_name="نطاق الخدمة (كم)")
    
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="السعر بالساعة")
    is_available = models.BooleanField(default=True, verbose_name="متاح؟")
    
    class Meta:
        verbose_name = "توفر أخصائي"
        verbose_name_plural = "توفر الأخصائيين"
        ordering = ['date', 'start_time']
    
    def __str__(self):
        return f"{self.specialist.user.username} - {self.date}"


# =================================================================
# 2. الجلسات (Sessions)
# =================================================================
class Session(TimeStampedModel):
    """الجلسات المنزلية"""
    specialist = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='sessions_as_specialist',
        verbose_name="الأخصائي",
        limit_choices_to={'role': 'specialist'}
    )
    patient = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='sessions_as_patient',
        verbose_name="المريض",
        limit_choices_to={'role': 'patient'}
    )
    availability = models.ForeignKey(SpecialistAvailability, on_delete=models.SET_NULL, null=True, verbose_name="التوفر")
    
    session_date = models.DateTimeField(verbose_name="تاريخ الجلسة")
    duration_hours = models.DecimalField(max_digits=4, decimal_places=2, default=1.0, verbose_name="المدة (ساعة)")
    
    # الموقع
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="خط العرض")
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="خط الطول")
    location_address = models.TextField(verbose_name="عنوان الجلسة")
    
    # المبلغ
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر بالساعة")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ الإجمالي")
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'قيد الانتظار'),
            ('confirmed', 'مؤكد'),
            ('in_progress', 'قيد التنفيذ'),
            ('completed', 'مكتمل'),
            ('cancelled', 'ملغي'),
        ],
        default='pending',
        verbose_name="الحالة"
    )
    
    notes = models.TextField(blank=True, verbose_name="ملاحظات")
    
    class Meta:
        verbose_name = "جلسة"
        verbose_name_plural = "الجلسات"
        ordering = ['session_date']
    
    def __str__(self):
        return f"Session: {self.patient.user.username} with {self.specialist.user.username}"
    
    def save(self, *args, **kwargs):
        if not self.total_amount:
            self.total_amount = self.hourly_rate * self.duration_hours
        super().save(*args, **kwargs)


# =================================================================
# 3. التقييمات (Session Reviews)
# =================================================================
class SessionReview(TimeStampedModel):
    """تقييمات الجلسات"""
    session = models.OneToOneField(Session, on_delete=models.CASCADE, related_name='review', verbose_name="الجلسة")
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='session_reviews', verbose_name="المقيّم")
    
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="التقييم")
    comment = models.TextField(verbose_name="التعليق")
    
    class Meta:
        verbose_name = "تقييم جلسة"
        verbose_name_plural = "تقييمات الجلسات"
    
    def __str__(self):
        return f"Review for Session #{self.session.id}"

