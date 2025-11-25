from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile, ROLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    """Serializer للمستخدم الأساسي"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer لملف تعريف المستخدم"""
    user = UserSerializer(read_only=True)
    role_display = serializers.CharField(source='get_role_display', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'role', 'role_display', 'phone_number', 
            'bio', 'is_verified', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer للتسجيل (Register)"""
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True, 
        required=True,
        style={'input_type': 'password'},
        label="تأكيد كلمة المرور"
    )
    role = serializers.ChoiceField(choices=ROLE_CHOICES, required=True)
    phone_number = serializers.CharField(max_length=20, required=False, allow_blank=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'role', 'phone_number']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': False},
            'last_name': {'required': False},
        }
    
    def validate(self, attrs):
        """التحقق من تطابق كلمات المرور"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "كلمات المرور غير متطابقة"
            })
        return attrs
    
    def validate_email(self, value):
        """التحقق من عدم وجود البريد الإلكتروني مسبقاً"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("هذا البريد الإلكتروني مستخدم بالفعل")
        return value
    
    def create(self, validated_data):
        """إنشاء مستخدم جديد وملف تعريفه"""
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        role = validated_data.pop('role')
        phone_number = validated_data.pop('phone_number', None)
        
        # إنشاء المستخدم
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=password,
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        
        # تحديث ملف التعريف (يتم إنشاؤه تلقائياً عبر signal)
        user.userprofile.role = role
        if phone_number:
            user.userprofile.phone_number = phone_number
        user.userprofile.save()
        
        return user


class ProfileUpdateSerializer(serializers.ModelSerializer):
    """Serializer لتحديث ملف التعريف"""
    user = UserSerializer()
    
    class Meta:
        model = UserProfile
        fields = ['user', 'phone_number', 'bio']
    
    def update(self, instance, validated_data):
        """تحديث ملف التعريف والمستخدم"""
        user_data = validated_data.pop('user', {})
        user = instance.user
        
        # تحديث بيانات المستخدم
        if user_data:
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()
        
        # تحديث ملف التعريف
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

