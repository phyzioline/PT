from django.db import models
from accounts.models import UserProfile  # لربط الوظيفة بجهة (شركة أو مركز)

# =================================================================
# 1. نموذج الوظيفة (Job Post)
# =================================================================
class JobPost(models.Model):
    # ربط الوظيفة بالجهة المعلنة (يجب أن يكون UserProfile دوره Company/Clinic)
    company = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='job_posts', verbose_name="الجهة المعلنة")
    
    title = models.CharField(max_length=255, verbose_name="عنوان الوظيفة")
    description = models.TextField(verbose_name="الوصف والتفاصيل")
    location = models.CharField(max_length=100, verbose_name="موقع العمل")
    is_full_time = models.BooleanField(default=True, verbose_name="دوام كامل؟")
    salary_range = models.CharField(max_length=100, blank=True, null=True, verbose_name="نطاق الراتب المتوقع")
    posted_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")

    def __str__(self):
        return f"{self.title} @ {self.company.user.username}"

    class Meta:
        verbose_name = "وظيفة شاغرة"
        verbose_name_plural = "الوظائف"
        ordering = ['-posted_at']

# =================================================================
# 2. نموذج طلب التقديم (Application)
# =================================================================
class JobApplication(models.Model):
    # ربط الطلب بالوظيفة
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications', verbose_name="الوظيفة المقدم لها")
    # ربط الطلب بالمتقدم (عادة يكون UserProfile دوره Specialist)
    applicant = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='my_applications', verbose_name="المتقدم")
    
    cover_letter = models.TextField(verbose_name="رسالة التقديم/السيرة الذاتية")
    applied_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التقديم")
    
    # حالة الطلب (ATS Tracking)
    STATUS_CHOICES = (
        ('pending', 'قيد المراجعة'),
        ('reviewed', 'تمت المراجعة'),
        ('interview', 'دعوة لمقابلة'),
        ('rejected', 'تم الرفض'),
        ('hired', 'تم التوظيف'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="الحالة")

    def __str__(self):
        return f"Application by {self.applicant.user.username} for {self.job.title}"

    class Meta:
        verbose_name = "طلب وظيفة"
        verbose_name_plural = "طلبات الوظائف"
        # ضمان أن المستخدم لا يتقدم للوظيفة مرتين
        unique_together = ('job', 'applicant')
