from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import UserProfile
from core_data.models import TimeStampedModel, SoftDeleteModel


# =================================================================
# 1. الكورسات (Courses)
# =================================================================
class Course(TimeStampedModel, SoftDeleteModel):
    """الكورسات التعليمية"""
    trainer = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name="المدرب",
        limit_choices_to={'role': 'trainer'}
    )
    
    title = models.CharField(max_length=255, verbose_name="عنوان الكورس")
    slug = models.SlugField(unique=True, verbose_name="رابط الكورس")
    description = models.TextField(verbose_name="الوصف")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="وصف مختصر")
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="السعر"
    )
    is_free = models.BooleanField(default=False, verbose_name="مجاني؟")
    
    thumbnail = models.ImageField(upload_to='courses/thumbnails/', blank=True, null=True, verbose_name="صورة الغلاف")
    duration_hours = models.PositiveIntegerField(default=0, verbose_name="عدد الساعات")
    level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'مبتدئ'),
            ('intermediate', 'متوسط'),
            ('advanced', 'متقدم'),
        ],
        default='beginner',
        verbose_name="المستوى"
    )
    
    is_published = models.BooleanField(default=False, verbose_name="منشور؟")
    is_featured = models.BooleanField(default=False, verbose_name="مميز؟")
    
    # إحصائيات
    students_count = models.PositiveIntegerField(default=0, verbose_name="عدد الطلاب")
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name="متوسط التقييم")
    
    class Meta:
        verbose_name = "كورس"
        verbose_name_plural = "الكورسات"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


# =================================================================
# 2. الدروس (Lessons)
# =================================================================
class Lesson(TimeStampedModel):
    """دروس الكورس"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name="الكورس")
    
    title = models.CharField(max_length=255, verbose_name="عنوان الدرس")
    description = models.TextField(blank=True, verbose_name="الوصف")
    video_url = models.URLField(blank=True, null=True, verbose_name="رابط الفيديو")
    video_file = models.FileField(upload_to='courses/videos/', blank=True, null=True, verbose_name="ملف الفيديو")
    duration_minutes = models.PositiveIntegerField(default=0, verbose_name="مدة الدرس (دقيقة)")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    is_preview = models.BooleanField(default=False, verbose_name="معاينة مجانية؟")
    
    class Meta:
        verbose_name = "درس"
        verbose_name_plural = "الدروس"
        ordering = ['order', 'id']
        unique_together = ['course', 'order']
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"


# =================================================================
# 3. المواد التعليمية (Materials)
# =================================================================
class CourseMaterial(models.Model):
    """المواد التعليمية (PDFs, Files)"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials', verbose_name="الدرس")
    
    title = models.CharField(max_length=255, verbose_name="العنوان")
    file = models.FileField(upload_to='courses/materials/', verbose_name="الملف")
    file_type = models.CharField(
        max_length=20,
        choices=[
            ('pdf', 'PDF'),
            ('doc', 'Word'),
            ('ppt', 'PowerPoint'),
            ('other', 'أخرى'),
        ],
        default='pdf',
        verbose_name="نوع الملف"
    )
    
    class Meta:
        verbose_name = "مادة تعليمية"
        verbose_name_plural = "المواد التعليمية"
    
    def __str__(self):
        return f"{self.lesson.title} - {self.title}"


# =================================================================
# 4. التسجيل في الكورس (Enrollment)
# =================================================================
class Enrollment(TimeStampedModel):
    """تسجيل الطلاب في الكورسات"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments', verbose_name="الكورس")
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='enrollments', verbose_name="الطالب")
    
    progress_percentage = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="نسبة الإنجاز (%)"
    )
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الإكمال")
    is_completed = models.BooleanField(default=False, verbose_name="مكتمل؟")
    
    class Meta:
        verbose_name = "تسجيل"
        verbose_name_plural = "التسجيلات"
        unique_together = ['course', 'student']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.student.user.username} - {self.course.title}"


# =================================================================
# 5. تقدم الطالب (Progress)
# =================================================================
class LessonProgress(models.Model):
    """تقدم الطالب في الدروس"""
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='lesson_progress', verbose_name="التسجيل")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="الدرس")
    
    is_completed = models.BooleanField(default=False, verbose_name="مكتمل؟")
    watched_duration = models.PositiveIntegerField(default=0, verbose_name="المدة المشاهدة (ثانية)")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الإكمال")
    
    class Meta:
        verbose_name = "تقدم في درس"
        verbose_name_plural = "التقدم في الدروس"
        unique_together = ['enrollment', 'lesson']
    
    def __str__(self):
        return f"{self.enrollment.student.user.username} - {self.lesson.title}"


# =================================================================
# 6. الشهادات (Certificates)
# =================================================================
class Certificate(TimeStampedModel):
    """شهادات إتمام الكورسات"""
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, related_name='certificate', verbose_name="التسجيل")
    
    certificate_number = models.CharField(max_length=50, unique=True, verbose_name="رقم الشهادة")
    issued_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإصدار")
    
    class Meta:
        verbose_name = "شهادة"
        verbose_name_plural = "الشهادات"
        ordering = ['-issued_at']
    
    def __str__(self):
        return f"Certificate #{self.certificate_number}"
    
    def save(self, *args, **kwargs):
        if not self.certificate_number:
            import random
            import string
            self.certificate_number = 'CERT-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        super().save(*args, **kwargs)


# =================================================================
# 7. تقييمات الكورسات (Course Reviews)
# =================================================================
class CourseReview(TimeStampedModel):
    """تقييمات ومراجعات الكورسات"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_reviews', verbose_name="الكورس")
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='course_reviews', verbose_name="الطالب")
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, null=True, blank=True, verbose_name="التسجيل")
    
    rating = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        verbose_name="التقييم"
    )
    comment = models.TextField(verbose_name="التعليق")
    is_approved = models.BooleanField(default=False, verbose_name="موافق عليه؟")
    
    class Meta:
        verbose_name = "تقييم كورس"
        verbose_name_plural = "تقييمات الكورسات"
        unique_together = ['course', 'student']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Review by {self.student.user.username} for {self.course.title}"

