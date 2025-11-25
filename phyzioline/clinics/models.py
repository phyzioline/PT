from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import UserProfile
from core_data.models import TimeStampedModel, SoftDeleteModel


# =================================================================
# 1. العيادات (Clinics)
# =================================================================
class Clinic(TimeStampedModel, SoftDeleteModel):
    """العيادات والمراكز الطبية"""
    company = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='clinics',
        verbose_name="الشركة",
        limit_choices_to={'role': 'company'}
    )
    
    name = models.CharField(max_length=255, verbose_name="اسم العيادة")
    slug = models.SlugField(unique=True, verbose_name="رابط العيادة")
    description = models.TextField(verbose_name="الوصف")
    
    address = models.TextField(verbose_name="العنوان")
    city = models.CharField(max_length=100, verbose_name="المدينة")
    country = models.CharField(max_length=100, default="مصر", verbose_name="الدولة")
    phone = models.CharField(max_length=20, verbose_name="الهاتف")
    email = models.EmailField(blank=True, verbose_name="البريد الإلكتروني")
    
    # Subscription
    subscription_tier = models.CharField(
        max_length=20,
        choices=[
            ('basic', 'أساسي'),
            ('professional', 'احترافي'),
            ('enterprise', 'مؤسسي'),
        ],
        default='basic',
        verbose_name="نوع الاشتراك"
    )
    subscription_start = models.DateTimeField(null=True, blank=True, verbose_name="بداية الاشتراك")
    subscription_end = models.DateTimeField(null=True, blank=True, verbose_name="نهاية الاشتراك")
    is_active = models.BooleanField(default=True, verbose_name="نشط؟")
    
    class Meta:
        verbose_name = "عيادة"
        verbose_name_plural = "العيادات"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


# =================================================================
# 2. المرضى (Patients)
# =================================================================
class Patient(TimeStampedModel):
    """المرضى (خاص بكل عيادة)"""
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='patients', verbose_name="العيادة")
    
    first_name = models.CharField(max_length=100, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=100, verbose_name="الاسم الأخير")
    phone = models.CharField(max_length=20, verbose_name="الهاتف")
    email = models.EmailField(blank=True, verbose_name="البريد الإلكتروني")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="تاريخ الميلاد")
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'ذكر'), ('female', 'أنثى')],
        blank=True,
        verbose_name="الجنس"
    )
    address = models.TextField(blank=True, verbose_name="العنوان")
    medical_history = models.TextField(blank=True, verbose_name="التاريخ الطبي")
    
    class Meta:
        verbose_name = "مريض"
        verbose_name_plural = "المرضى"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# =================================================================
# 3. المواعيد (Appointments)
# =================================================================
class Appointment(TimeStampedModel):
    """المواعيد"""
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='appointments', verbose_name="العيادة")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments', verbose_name="المريض")
    doctor = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='appointments',
        verbose_name="الطبيب",
        limit_choices_to={'role': 'doctor'}
    )
    
    appointment_date = models.DateTimeField(verbose_name="تاريخ الموعد")
    duration_minutes = models.PositiveIntegerField(default=30, verbose_name="المدة (دقيقة)")
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'مجدول'),
            ('confirmed', 'مؤكد'),
            ('in_progress', 'قيد التنفيذ'),
            ('completed', 'مكتمل'),
            ('cancelled', 'ملغي'),
            ('no_show', 'لم يحضر'),
        ],
        default='scheduled',
        verbose_name="الحالة"
    )
    
    notes = models.TextField(blank=True, verbose_name="ملاحظات")
    
    class Meta:
        verbose_name = "موعد"
        verbose_name_plural = "المواعيد"
        ordering = ['appointment_date']
    
    def __str__(self):
        return f"{self.patient} - {self.appointment_date}"


# =================================================================
# 4. الملاحظات الطبية (Medical Notes)
# =================================================================
class MedicalNote(TimeStampedModel):
    """الملاحظات والملفات الطبية"""
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='medical_notes', verbose_name="الموعد")
    doctor = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, verbose_name="الطبيب")
    
    diagnosis = models.TextField(verbose_name="التشخيص")
    treatment_plan = models.TextField(verbose_name="خطة العلاج")
    prescription = models.TextField(blank=True, verbose_name="الوصفة الطبية")
    notes = models.TextField(blank=True, verbose_name="ملاحظات إضافية")
    
    class Meta:
        verbose_name = "ملاحظة طبية"
        verbose_name_plural = "الملاحظات الطبية"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Note for {self.appointment.patient} - {self.created_at}"


# =================================================================
# 5. الفواتير (Billing)
# =================================================================
class Invoice(TimeStampedModel):
    """الفواتير والمدفوعات"""
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='invoices', verbose_name="العيادة")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='invoices', verbose_name="المريض")
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الموعد")
    
    invoice_number = models.CharField(max_length=50, unique=True, verbose_name="رقم الفاتورة")
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="المبلغ")
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="الضريبة")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الإجمالي")
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'قيد الانتظار'),
            ('paid', 'مدفوع'),
            ('overdue', 'متأخر'),
            ('cancelled', 'ملغي'),
        ],
        default='pending',
        verbose_name="الحالة"
    )
    
    paid_at = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الدفع")
    payment_method = models.CharField(max_length=50, blank=True, verbose_name="طريقة الدفع")
    
    class Meta:
        verbose_name = "فاتورة"
        verbose_name_plural = "الفواتير"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Invoice #{self.invoice_number}"
    
    def save(self, *args, **kwargs):
        if not self.invoice_number:
            import random
            import string
            self.invoice_number = 'INV-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.total = self.amount + self.tax
        super().save(*args, **kwargs)

