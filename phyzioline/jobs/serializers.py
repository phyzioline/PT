from rest_framework import serializers
from .models import JobPost, JobApplication
from accounts.serializers import UserProfileSerializer


class JobPostSerializer(serializers.ModelSerializer):
    """Serializer للوظائف"""
    company = UserProfileSerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True, required=False)
    applications_count = serializers.IntegerField(source='applications.count', read_only=True)
    
    class Meta:
        model = JobPost
        fields = [
            'id', 'company', 'company_id', 'title', 'description', 
            'location', 'is_full_time', 'salary_range', 'posted_at', 
            'applications_count'
        ]
        read_only_fields = ['id', 'posted_at', 'company']
    
    def create(self, validated_data):
        """إنشاء وظيفة جديدة"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # استخدام company من المستخدم الحالي
            validated_data['company'] = request.user.userprofile
        elif 'company_id' in validated_data:
            from accounts.models import UserProfile
            validated_data['company'] = UserProfile.objects.get(id=validated_data.pop('company_id'))
        return super().create(validated_data)


class JobApplicationSerializer(serializers.ModelSerializer):
    """Serializer لطلبات التقديم"""
    job = JobPostSerializer(read_only=True)
    job_id = serializers.IntegerField(write_only=True)
    applicant = UserProfileSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = JobApplication
        fields = [
            'id', 'job', 'job_id', 'applicant', 'cover_letter', 
            'status', 'status_display', 'applied_at'
        ]
        read_only_fields = ['id', 'applicant', 'applied_at']
    
    def create(self, validated_data):
        """إنشاء طلب تقديم"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['applicant'] = request.user.userprofile
        return super().create(validated_data)
    
    def validate_job_id(self, value):
        """التحقق من وجود الوظيفة"""
        try:
            JobPost.objects.get(id=value)
        except JobPost.DoesNotExist:
            raise serializers.ValidationError("الوظيفة غير موجودة")
        return value


class JobApplicationStatusSerializer(serializers.ModelSerializer):
    """Serializer لتحديث حالة طلب التقديم فقط"""
    class Meta:
        model = JobApplication
        fields = ['status']
    
    def validate_status(self, value):
        """التحقق من صحة الحالة"""
        valid_statuses = [choice[0] for choice in JobApplication.STATUS_CHOICES]
        if value not in valid_statuses:
            raise serializers.ValidationError("حالة غير صحيحة")
        return value

