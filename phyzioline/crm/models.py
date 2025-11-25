from django.db import models
from accounts.models import UserProfile
from core_data.models import TimeStampedModel


# =================================================================
# 1. جهات الاتصال (Contacts)
# =================================================================
class Contact(TimeStampedModel):
    """جهات الاتصال في CRM"""
    first_name = models.CharField(max_length=100, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="الاسم الأخير")
    email = models.EmailField(blank=True, null=True, verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="الهاتف")
    
    source = models.CharField(
        max_length=50,
        choices=[
            ('website', 'الموقع'),
            ('whatsapp', 'WhatsApp'),
            ('facebook', 'Facebook'),
            ('referral', 'إحالة'),
            ('other', 'أخرى'),
        ],
        default='website',
        verbose_name="المصدر"
    )
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'جديد'),
            ('contacted', 'تم الاتصال'),
            ('qualified', 'مؤهل'),
            ('converted', 'محول'),
            ('lost', 'مفقود'),
        ],
        default='new',
        verbose_name="الحالة"
    )
    
    notes = models.TextField(blank=True, verbose_name="ملاحظات")
    assigned_to = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_contacts',
        verbose_name="مخصص لـ"
    )
    
    class Meta:
        verbose_name = "جهة اتصال"
        verbose_name_plural = "جهات الاتصال"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# =================================================================
# 2. الرسائل (Messages)
# =================================================================
class Message(TimeStampedModel):
    """الرسائل (WhatsApp, Email, etc.)"""
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='messages', verbose_name="جهة الاتصال")
    
    channel = models.CharField(
        max_length=20,
        choices=[
            ('whatsapp', 'WhatsApp'),
            ('email', 'Email'),
            ('sms', 'SMS'),
            ('facebook', 'Facebook'),
        ],
        verbose_name="القناة"
    )
    
    direction = models.CharField(
        max_length=10,
        choices=[
            ('inbound', 'وارد'),
            ('outbound', 'صادر'),
        ],
        verbose_name="الاتجاه"
    )
    
    content = models.TextField(verbose_name="المحتوى")
    status = models.CharField(
        max_length=20,
        choices=[
            ('sent', 'مرسل'),
            ('delivered', 'تم التسليم'),
            ('read', 'مقروء'),
            ('failed', 'فشل'),
        ],
        default='sent',
        verbose_name="الحالة"
    )
    
    metadata = models.JSONField(default=dict, blank=True, verbose_name="بيانات إضافية")
    
    class Meta:
        verbose_name = "رسالة"
        verbose_name_plural = "الرسائل"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message via {self.channel} - {self.direction}"


# =================================================================
# 3. الحملات (Campaigns)
# =================================================================
class CRMCampaign(TimeStampedModel):
    """حملات التسويق"""
    name = models.CharField(max_length=255, verbose_name="اسم الحملة")
    description = models.TextField(blank=True, verbose_name="الوصف")
    
    channel = models.CharField(
        max_length=20,
        choices=[
            ('whatsapp', 'WhatsApp'),
            ('email', 'Email'),
            ('sms', 'SMS'),
        ],
        verbose_name="القناة"
    )
    
    message_template = models.TextField(verbose_name="نموذج الرسالة")
    target_audience = models.JSONField(default=dict, blank=True, verbose_name="الجمهور المستهدف")
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'مسودة'),
            ('scheduled', 'مجدول'),
            ('running', 'قيد التشغيل'),
            ('completed', 'مكتمل'),
            ('cancelled', 'ملغي'),
        ],
        default='draft',
        verbose_name="الحالة"
    )
    
    sent_count = models.PositiveIntegerField(default=0, verbose_name="عدد المرسل")
    delivered_count = models.PositiveIntegerField(default=0, verbose_name="عدد الموصول")
    
    class Meta:
        verbose_name = "حملة CRM"
        verbose_name_plural = "حملات CRM"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

