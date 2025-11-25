from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# =================================================================
# أنواع الأدوار في التطبيق
# =================================================================
ROLE_CHOICES = (
    ('patient', 'مريض'),
    ('doctor', 'طبيب'),
    ('specialist', 'أخصائي علاج طبيعي'), # للتوظيف والعمل الحر
    ('vendor', 'مورد أجهزة'), 
    ('company', 'شركة/مركز طبي'), # لنشر الوظائف وتأجير العيادات
    ('trainer', 'مدرب/محاضر'), # لنشر الكورسات
    ('admin', 'مسؤول النظام'),
)

# =================================================================
# 1. نموذج ملف تعريف المستخدم (UserProfile)
# لتخزين الأدوار والبيانات الإضافية لكل مستخدم
# =================================================================
class UserProfile(models.Model):
    # ربط ملف التعريف بمستخدم Django الأساسي
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم الأساسي")
    # حقل الدور
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient', verbose_name="الدور")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الهاتف")
    bio = models.TextField(blank=True, null=True, verbose_name="نبذة تعريفية")
    
    # حقول إضافية قد تكون مطلوبة لأدوار محددة
    is_verified = models.BooleanField(default=False, verbose_name="تم التحقق من الوثائق")
    
    # حقول الوقت
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

    class Meta:
        verbose_name = "ملف تعريف المستخدم"
        verbose_name_plural = "ملفات تعريف المستخدمين"
        ordering = ['-created_at']

# =================================================================
# إشارات (Signals) لإنشاء ملف تعريف تلقائياً عند إنشاء مستخدم جديد
# =================================================================
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
