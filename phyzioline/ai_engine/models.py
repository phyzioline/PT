from django.db import models
from accounts.models import UserProfile
from core_data.models import TimeStampedModel


# =================================================================
# 1. خطط العلاج (Treatment Plans)
# =================================================================
class TreatmentPlan(TimeStampedModel):
    """خطط العلاج المولدة بالذكاء الاصطناعي"""
    patient = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='treatment_plans',
        verbose_name="المريض",
        limit_choices_to={'role': 'patient'}
    )
    doctor = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_treatment_plans',
        verbose_name="الطبيب",
        limit_choices_to={'role': 'doctor'}
    )
    
    condition = models.CharField(max_length=255, verbose_name="الحالة")
    diagnosis = models.TextField(verbose_name="التشخيص")
    treatment_plan = models.TextField(verbose_name="خطة العلاج")
    exercises = models.JSONField(default=list, blank=True, verbose_name="التمارين")
    duration_weeks = models.PositiveIntegerField(default=4, verbose_name="المدة (أسابيع)")
    
    is_ai_generated = models.BooleanField(default=True, verbose_name="مولّد بالذكاء الاصطناعي؟")
    
    class Meta:
        verbose_name = "خطة علاج"
        verbose_name_plural = "خطط العلاج"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Treatment Plan for {self.patient.user.username} - {self.condition}"


# =================================================================
# 2. التمارين (Exercises)
# =================================================================
class Exercise(models.Model):
    """مكتبة التمارين"""
    name = models.CharField(max_length=255, verbose_name="اسم التمرين")
    description = models.TextField(verbose_name="الوصف")
    instructions = models.TextField(verbose_name="التعليمات")
    image = models.ImageField(upload_to='exercises/', blank=True, null=True, verbose_name="صورة")
    video_url = models.URLField(blank=True, null=True, verbose_name="رابط الفيديو")
    
    category = models.CharField(
        max_length=50,
        choices=[
            ('strength', 'تقوية'),
            ('flexibility', 'مرونة'),
            ('balance', 'توازن'),
            ('cardio', 'قلبي وعائي'),
            ('rehabilitation', 'إعادة تأهيل'),
        ],
        verbose_name="الفئة"
    )
    
    difficulty_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'مبتدئ'),
            ('intermediate', 'متوسط'),
            ('advanced', 'متقدم'),
        ],
        default='beginner',
        verbose_name="مستوى الصعوبة"
    )
    
    duration_minutes = models.PositiveIntegerField(default=10, verbose_name="المدة (دقيقة)")
    repetitions = models.PositiveIntegerField(default=10, verbose_name="عدد التكرارات")
    
    class Meta:
        verbose_name = "تمرين"
        verbose_name_plural = "التمارين"
        ordering = ['name']
    
    def __str__(self):
        return self.name


# =================================================================
# 3. سجلات البحث (Search Logs)
# =================================================================
class SearchLog(TimeStampedModel):
    """سجلات البحث بالذكاء الاصطناعي"""
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='search_logs',
        verbose_name="المستخدم"
    )
    
    query = models.TextField(verbose_name="استعلام البحث")
    results_count = models.PositiveIntegerField(default=0, verbose_name="عدد النتائج")
    response_time_ms = models.PositiveIntegerField(default=0, verbose_name="وقت الاستجابة (ميللي ثانية)")
    
    class Meta:
        verbose_name = "سجل بحث"
        verbose_name_plural = "سجلات البحث"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Search: {self.query[:50]}"

