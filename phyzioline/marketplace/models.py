from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import UserProfile
from core_data.models import TimeStampedModel, SoftDeleteModel


# =================================================================
# 1. فئات المنتجات (Categories)
# =================================================================
class Category(models.Model):
    """فئات المنتجات (هيراركية)"""
    name = models.CharField(max_length=100, verbose_name="اسم الفئة")
    slug = models.SlugField(unique=True, verbose_name="رابط الفئة")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children',
        verbose_name="الفئة الأب"
    )
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="صورة الفئة")
    is_active = models.BooleanField(default=True, verbose_name="نشط؟")
    
    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"
        ordering = ['name']
    
    def __str__(self):
        return self.name


# =================================================================
# 2. المنتجات (Products)
# =================================================================
class Product(TimeStampedModel, SoftDeleteModel):
    """منتجات الأجهزة الطبية"""
    vendor = models.ForeignKey(
        UserProfile, 
        on_delete=models.CASCADE, 
        related_name='products',
        verbose_name="المورد",
        limit_choices_to={'role': 'vendor'}
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="الفئة")
    
    name = models.CharField(max_length=255, verbose_name="اسم المنتج")
    slug = models.SlugField(unique=True, verbose_name="رابط المنتج")
    description = models.TextField(verbose_name="الوصف")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="وصف مختصر")
    
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        verbose_name="السعر"
    )
    compare_at_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(0)],
        verbose_name="السعر قبل الخصم"
    )
    
    sku = models.CharField(max_length=100, unique=True, verbose_name="رمز المنتج")
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="الكمية المتاحة")
    track_inventory = models.BooleanField(default=True, verbose_name="تتبع المخزون؟")
    
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="الوزن (كجم)")
    dimensions = models.CharField(max_length=100, blank=True, verbose_name="الأبعاد")
    
    is_active = models.BooleanField(default=True, verbose_name="نشط؟")
    is_featured = models.BooleanField(default=False, verbose_name="منتج مميز؟")
    
    # SEO
    meta_title = models.CharField(max_length=255, blank=True, verbose_name="عنوان SEO")
    meta_description = models.TextField(blank=True, verbose_name="وصف SEO")
    
    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug', 'is_active']),
            models.Index(fields=['category', 'is_active']),
        ]
    
    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        """التحقق من توفر المنتج"""
        if not self.track_inventory:
            return True
        return self.stock_quantity > 0
    
    @property
    def discount_percentage(self):
        """نسبة الخصم"""
        if self.compare_at_price and self.compare_at_price > self.price:
            return int(((self.compare_at_price - self.price) / self.compare_at_price) * 100)
        return 0


# =================================================================
# 3. صور المنتجات (Product Images)
# =================================================================
class ProductImage(models.Model):
    """صور المنتجات"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="المنتج")
    image = models.ImageField(upload_to='products/', verbose_name="الصورة")
    alt_text = models.CharField(max_length=255, blank=True, verbose_name="النص البديل")
    is_primary = models.BooleanField(default=False, verbose_name="صورة رئيسية؟")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    
    class Meta:
        verbose_name = "صورة منتج"
        verbose_name_plural = "صور المنتجات"
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"{self.product.name} - Image {self.id}"


# =================================================================
# 4. سلة التسوق (Cart)
# =================================================================
class Cart(TimeStampedModel):
    """سلة التسوق"""
    user = models.OneToOneField(
        UserProfile, 
        on_delete=models.CASCADE, 
        related_name='cart',
        verbose_name="المستخدم"
    )
    
    class Meta:
        verbose_name = "سلة التسوق"
        verbose_name_plural = "سلال التسوق"
    
    def __str__(self):
        return f"Cart - {self.user.user.username}"
    
    @property
    def total(self):
        """إجمالي السلة"""
        return sum(item.subtotal for item in self.items.all())
    
    @property
    def items_count(self):
        """عدد العناصر"""
        return self.items.count()


class CartItem(models.Model):
    """عناصر سلة التسوق"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name="السلة")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name="الكمية")
    
    class Meta:
        verbose_name = "عنصر سلة"
        verbose_name_plural = "عناصر السلة"
        unique_together = ['cart', 'product']
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
    @property
    def subtotal(self):
        """المجموع الفرعي"""
        return self.product.price * self.quantity


# =================================================================
# 5. الطلبات (Orders)
# =================================================================
class Order(TimeStampedModel):
    """الطلبات"""
    ORDER_STATUS_CHOICES = (
        ('pending', 'قيد الانتظار'),
        ('confirmed', 'تم التأكيد'),
        ('processing', 'قيد المعالجة'),
        ('shipped', 'تم الشحن'),
        ('delivered', 'تم التسليم'),
        ('cancelled', 'ملغي'),
        ('refunded', 'مسترد'),
    )
    
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'قيد الانتظار'),
        ('paid', 'مدفوع'),
        ('failed', 'فشل'),
        ('refunded', 'مسترد'),
    )
    
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='orders', verbose_name="المستخدم")
    order_number = models.CharField(max_length=50, unique=True, verbose_name="رقم الطلب")
    
    # الحالة
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending', verbose_name="حالة الطلب")
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending', verbose_name="حالة الدفع")
    
    # المبالغ
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المجموع الفرعي")
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="تكلفة الشحن")
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="الضريبة")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الإجمالي")
    
    # معلومات الشحن
    shipping_name = models.CharField(max_length=255, verbose_name="اسم المستلم")
    shipping_phone = models.CharField(max_length=20, verbose_name="هاتف المستلم")
    shipping_address = models.TextField(verbose_name="عنوان الشحن")
    shipping_city = models.CharField(max_length=100, verbose_name="المدينة")
    shipping_country = models.CharField(max_length=100, default="مصر", verbose_name="الدولة")
    shipping_postal_code = models.CharField(max_length=20, blank=True, verbose_name="الرمز البريدي")
    
    # ملاحظات
    notes = models.TextField(blank=True, verbose_name="ملاحظات")
    
    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order #{self.order_number}"
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            import random
            import string
            self.order_number = 'ORD-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    """عناصر الطلب"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="المنتج")
    product_name = models.CharField(max_length=255, verbose_name="اسم المنتج (حفظ)")
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر المنتج (حفظ)")
    quantity = models.PositiveIntegerField(verbose_name="الكمية")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المجموع الفرعي")
    
    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"
    
    def __str__(self):
        return f"{self.product_name} x {self.quantity}"


# =================================================================
# 6. المدفوعات (Payments)
# =================================================================
class Payment(TimeStampedModel):
    """المدفوعات"""
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'نقدي عند الاستلام'),
        ('card', 'بطاقة ائتمان'),
        ('bank_transfer', 'تحويل بنكي'),
        ('wallet', 'محفظة إلكترونية'),
    )
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment', verbose_name="الطلب")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name="طريقة الدفع")
    transaction_id = models.CharField(max_length=255, blank=True, verbose_name="رقم المعاملة")
    status = models.CharField(max_length=20, choices=Order.PAYMENT_STATUS_CHOICES, default='pending', verbose_name="الحالة")
    paid_at = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الدفع")
    
    class Meta:
        verbose_name = "دفعة"
        verbose_name_plural = "المدفوعات"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Payment for Order #{self.order.order_number}"


# =================================================================
# 7. التقييمات والمراجعات (Reviews)
# =================================================================
class Review(TimeStampedModel):
    """تقييمات ومراجعات المنتجات"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name="المنتج")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews', verbose_name="المستخدم")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name="الطلب")
    
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="التقييم")
    title = models.CharField(max_length=255, blank=True, verbose_name="عنوان المراجعة")
    comment = models.TextField(verbose_name="التعليق")
    is_verified_purchase = models.BooleanField(default=False, verbose_name="شراء موثق؟")
    is_approved = models.BooleanField(default=False, verbose_name="موافق عليه؟")
    
    class Meta:
        verbose_name = "مراجعة"
        verbose_name_plural = "المراجعات"
        unique_together = ['product', 'user']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Review by {self.user.user.username} for {self.product.name}"
