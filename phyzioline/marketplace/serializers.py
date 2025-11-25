from rest_framework import serializers
from django.db import models
from .models import (
    Category, Product, ProductImage, Cart, CartItem, 
    Order, OrderItem, Payment, Review
)
from accounts.serializers import UserProfileSerializer


class CategorySerializer(serializers.ModelSerializer):
    """Serializer للفئات"""
    children = serializers.SerializerMethodField()
    products_count = serializers.IntegerField(source='product_set.count', read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'parent', 'image', 'is_active', 'children', 'products_count']
        read_only_fields = ['id']
    
    def get_children(self, obj):
        """الحصول على الفئات الفرعية"""
        children = obj.children.filter(is_active=True)
        return CategorySerializer(children, many=True).data


class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer لصور المنتجات"""
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_primary', 'order']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    """Serializer للمنتجات"""
    vendor = UserProfileSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    images = ProductImageSerializer(many=True, read_only=True)
    is_in_stock = serializers.BooleanField(read_only=True)
    discount_percentage = serializers.IntegerField(read_only=True)
    average_rating = serializers.SerializerMethodField()
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'vendor', 'category', 'category_id', 'name', 'slug', 
            'description', 'short_description', 'price', 'compare_at_price',
            'sku', 'stock_quantity', 'track_inventory', 'weight', 'dimensions',
            'is_active', 'is_featured', 'is_in_stock', 'discount_percentage',
            'images', 'average_rating', 'reviews_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'vendor']
    
    def get_average_rating(self, obj):
        """متوسط التقييم"""
        reviews = obj.reviews.filter(is_approved=True)
        if reviews.exists():
            return round(reviews.aggregate(models.Avg('rating'))['rating__avg'], 1)
        return 0


class CartItemSerializer(serializers.ModelSerializer):
    """Serializer لعناصر السلة"""
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'subtotal']
        read_only_fields = ['id', 'subtotal']
    
    def validate_product_id(self, value):
        """التحقق من وجود المنتج وتوافره"""
        try:
            product = Product.objects.get(id=value, is_active=True, is_deleted=False)
            if not product.is_in_stock:
                raise serializers.ValidationError("المنتج غير متوفر حالياً")
        except Product.DoesNotExist:
            raise serializers.ValidationError("المنتج غير موجود")
        return value


class CartSerializer(serializers.ModelSerializer):
    """Serializer للسلة"""
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    items_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total', 'items_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer لعناصر الطلب"""
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'subtotal']
        read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    """Serializer للطلبات"""
    user = UserProfileSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    payment = serializers.SerializerMethodField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    payment_status_display = serializers.CharField(source='get_payment_status_display', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'order_number', 'status', 'status_display',
            'payment_status', 'payment_status_display', 'subtotal',
            'shipping_cost', 'tax', 'total', 'shipping_name', 'shipping_phone',
            'shipping_address', 'shipping_city', 'shipping_country',
            'shipping_postal_code', 'notes', 'items', 'payment',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'order_number', 'created_at', 'updated_at', 'user']
    
    def get_payment(self, obj):
        """الحصول على معلومات الدفع"""
        if hasattr(obj, 'payment'):
            return PaymentSerializer(obj.payment).data
        return None


class CreateOrderSerializer(serializers.Serializer):
    """Serializer لإنشاء طلب جديد من السلة"""
    shipping_name = serializers.CharField(max_length=255)
    shipping_phone = serializers.CharField(max_length=20)
    shipping_address = serializers.CharField()
    shipping_city = serializers.CharField(max_length=100)
    shipping_country = serializers.CharField(max_length=100, default="مصر")
    shipping_postal_code = serializers.CharField(max_length=20, required=False, allow_blank=True)
    notes = serializers.CharField(required=False, allow_blank=True)
    payment_method = serializers.ChoiceField(choices=Payment.PAYMENT_METHOD_CHOICES)


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer للمدفوعات"""
    method_display = serializers.CharField(source='get_method_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Payment
        fields = [
            'id', 'order', 'amount', 'method', 'method_display',
            'transaction_id', 'status', 'status_display', 'paid_at',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer للمراجعات"""
    user = UserProfileSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id', 'product', 'user', 'order', 'rating', 'title',
            'comment', 'is_verified_purchase', 'is_approved', 'created_at'
        ]
        read_only_fields = ['id', 'user', 'is_approved', 'created_at']
    
    def validate(self, attrs):
        """التحقق من أن المستخدم اشترى المنتج"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # يمكن إضافة منطق للتحقق من الشراء
            pass
        return attrs

