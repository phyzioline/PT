from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter
from django.db import transaction, models
from django.utils import timezone
from .models import (
    Category, Product, ProductImage, Cart, CartItem,
    Order, OrderItem, Payment, Review
)
from .serializers import (
    CategorySerializer, ProductSerializer, ProductImageSerializer,
    CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer,
    CreateOrderSerializer, PaymentSerializer, ReviewSerializer
)
from core_data.permissions import IsVendor, IsOwnerOrReadOnly
from core_data.utils import success_response, error_response


# =================================================================
# Filters
# =================================================================
class ProductFilter(FilterSet):
    """فلاتر للمنتجات"""
    category = CharFilter(field_name='category__slug')
    vendor = NumberFilter(field_name='vendor__id')
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    is_featured = BooleanFilter(field_name='is_featured')
    in_stock = BooleanFilter(method='filter_in_stock')
    search = CharFilter(method='filter_search')
    
    def filter_in_stock(self, queryset, name, value):
        """فلتر المنتجات المتوفرة"""
        if value:
            return queryset.filter(stock_quantity__gt=0)
        return queryset
    
    def filter_search(self, queryset, name, value):
        """بحث في اسم ووصف المنتج"""
        return queryset.filter(
            models.Q(name__icontains=value) |
            models.Q(description__icontains=value) |
            models.Q(short_description__icontains=value)
        )
    
    class Meta:
        model = Product
        fields = ['category', 'vendor', 'min_price', 'max_price', 'is_featured', 'in_stock']


# =================================================================
# Viewsets
# =================================================================
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet للفئات (قراءة فقط)"""
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    @action(detail=True, methods=['get'])
    def products(self, request, slug=None):
        """الحصول على منتجات الفئة"""
        category = self.get_object()
        products = Product.objects.filter(
            category=category, 
            is_active=True, 
            is_deleted=False
        )
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return success_response(data=serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet للمنتجات"""
    queryset = Product.objects.filter(is_deleted=False, is_active=True)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'short_description', 'sku']
    ordering_fields = ['created_at', 'price', 'name']
    ordering = ['-created_at']
    lookup_field = 'slug'
    
    def get_permissions(self):
        """تحديد الصلاحيات"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsVendor()]
        return [AllowAny()]
    
    def get_queryset(self):
        """تصفية المنتجات"""
        queryset = super().get_queryset()
        
        # إذا كان vendor، يمكنه رؤية جميع منتجاته
        if self.action == 'my_products' and self.request.user.is_authenticated:
            if hasattr(self.request.user, 'userprofile'):
                return queryset.filter(vendor=self.request.user.userprofile)
        
        return queryset
    
    def perform_create(self, serializer):
        """إنشاء منتج جديد"""
        serializer.save(vendor=self.request.user.userprofile)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated, IsVendor])
    def my_products(self, request):
        """الحصول على منتجات المورد الحالي"""
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)
        return success_response(data=serializer.data)


class CartViewSet(viewsets.ModelViewSet):
    """ViewSet للسلة"""
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """الحصول على سلة المستخدم الحالي"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            cart, created = Cart.objects.get_or_create(user=self.request.user.userprofile)
            return Cart.objects.filter(id=cart.id)
        return Cart.objects.none()
    
    def get_object(self):
        """الحصول على سلة المستخدم الحالي"""
        cart, created = Cart.objects.get_or_create(user=self.request.user.userprofile)
        return cart
    
    @action(detail=False, methods=['post'], url_path='add-item')
    def add_item(self, request):
        """إضافة منتج إلى السلة"""
        cart, created = Cart.objects.get_or_create(user=request.user.userprofile)
        
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        
        try:
            product = Product.objects.get(id=product_id, is_active=True, is_deleted=False)
        except Product.DoesNotExist:
            return error_response(message="المنتج غير موجود")
        
        if not product.is_in_stock:
            return error_response(message="المنتج غير متوفر حالياً")
        
        if product.track_inventory and quantity > product.stock_quantity:
            return error_response(message=f"الكمية المتاحة: {product.stock_quantity}")
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            if product.track_inventory and cart_item.quantity > product.stock_quantity:
                cart_item.quantity = product.stock_quantity
            cart_item.save()
        
        serializer = CartSerializer(cart)
        return success_response(data=serializer.data, message="تمت الإضافة بنجاح")
    
    @action(detail=False, methods=['post'], url_path='update-item')
    def update_item(self, request):
        """تحديث كمية عنصر في السلة"""
        cart = self.get_object()
        item_id = request.data.get('item_id')
        quantity = int(request.data.get('quantity', 1))
        
        try:
            cart_item = CartItem.objects.get(id=item_id, cart=cart)
        except CartItem.DoesNotExist:
            return error_response(message="العنصر غير موجود")
        
        if quantity <= 0:
            cart_item.delete()
            return success_response(message="تم حذف العنصر")
        
        if cart_item.product.track_inventory and quantity > cart_item.product.stock_quantity:
            return error_response(message=f"الكمية المتاحة: {cart_item.product.stock_quantity}")
        
        cart_item.quantity = quantity
        cart_item.save()
        
        serializer = CartSerializer(cart)
        return success_response(data=serializer.data, message="تم التحديث بنجاح")
    
    @action(detail=False, methods=['post'], url_path='remove-item')
    def remove_item(self, request):
        """حذف عنصر من السلة"""
        cart = self.get_object()
        item_id = request.data.get('item_id')
        
        try:
            cart_item = CartItem.objects.get(id=item_id, cart=cart)
            cart_item.delete()
            return success_response(message="تم الحذف بنجاح")
        except CartItem.DoesNotExist:
            return error_response(message="العنصر غير موجود")
    
    @action(detail=False, methods=['post'], url_path='clear')
    def clear_cart(self, request):
        """تفريغ السلة"""
        cart = self.get_object()
        cart.items.all().delete()
        return success_response(message="تم تفريغ السلة")


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet للطلبات"""
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'payment_status']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على طلبات المستخدم الحالي"""
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            return Order.objects.filter(user=self.request.user.userprofile)
        return Order.objects.none()
    
    @action(detail=False, methods=['post'], url_path='checkout')
    def checkout(self, request):
        """إنشاء طلب جديد من السلة"""
        cart, created = Cart.objects.get_or_create(user=request.user.userprofile)
        
        if cart.items.count() == 0:
            return error_response(message="السلة فارغة")
        
        serializer = CreateOrderSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(errors=serializer.errors)
        
        # التحقق من توفر المنتجات
        for item in cart.items.all():
            if not item.product.is_in_stock:
                return error_response(message=f"المنتج {item.product.name} غير متوفر")
            if item.product.track_inventory and item.quantity > item.product.stock_quantity:
                return error_response(message=f"الكمية المتاحة من {item.product.name}: {item.product.stock_quantity}")
        
        with transaction.atomic():
            # إنشاء الطلب
            order = Order.objects.create(
                user=request.user.userprofile,
                subtotal=cart.total,
                shipping_cost=0,  # يمكن حسابها لاحقاً
                tax=0,  # يمكن حسابها لاحقاً
                total=cart.total,
                shipping_name=serializer.validated_data['shipping_name'],
                shipping_phone=serializer.validated_data['shipping_phone'],
                shipping_address=serializer.validated_data['shipping_address'],
                shipping_city=serializer.validated_data['shipping_city'],
                shipping_country=serializer.validated_data.get('shipping_country', 'مصر'),
                shipping_postal_code=serializer.validated_data.get('shipping_postal_code', ''),
                notes=serializer.validated_data.get('notes', '')
            )
            
            # إنشاء عناصر الطلب
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    product_name=item.product.name,
                    product_price=item.product.price,
                    quantity=item.quantity,
                    subtotal=item.subtotal
                )
                
                # تحديث المخزون
                if item.product.track_inventory:
                    item.product.stock_quantity -= item.quantity
                    item.product.save()
            
            # إنشاء الدفعة
            Payment.objects.create(
                order=order,
                amount=order.total,
                method=serializer.validated_data['payment_method']
            )
            
            # تفريغ السلة
            cart.items.all().delete()
        
        order_serializer = OrderSerializer(order)
        return success_response(
            data=order_serializer.data,
            message="تم إنشاء الطلب بنجاح",
            status_code=status.HTTP_201_CREATED
        )


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet للمراجعات"""
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['product', 'rating', 'is_approved']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """الحصول على المراجعات الموافق عليها"""
        queryset = Review.objects.filter(is_approved=True)
        
        # إذا كان vendor، يمكنه رؤية جميع مراجعات منتجاته
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            if self.request.user.userprofile.role == 'vendor':
                queryset = Review.objects.filter(product__vendor=self.request.user.userprofile)
        
        return queryset
    
    def perform_create(self, serializer):
        """إنشاء مراجعة جديدة"""
        serializer.save(user=self.request.user.userprofile)
