"""
Base Models مشتركة بين جميع التطبيقات
"""
from django.db import models


class TimeStampedModel(models.Model):
    """نموذج أساسي يضيف created_at و updated_at تلقائياً"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    
    class Meta:
        abstract = True
        ordering = ['-created_at']


class SoftDeleteModel(models.Model):
    """نموذج أساسي للـ Soft Delete (حذف منطقي)"""
    is_deleted = models.BooleanField(default=False, verbose_name="محذوف؟")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الحذف")
    
    class Meta:
        abstract = True
    
    def soft_delete(self):
        """حذف منطقي"""
        from django.utils import timezone
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
    
    def restore(self):
        """استعادة المحذوف"""
        self.is_deleted = False
        self.deleted_at = None
        self.save()

