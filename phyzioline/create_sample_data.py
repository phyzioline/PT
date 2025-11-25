import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phyzioline_core.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile
from marketplace.models import Category, Product
from jobs.models import JobPost
from courses.models import Course
from clinics.models import Clinic
from feed.models import Post

print("📦 إنشاء بيانات تجريبية...\n")

# إنشاء Vendor
vendor_user, created = User.objects.get_or_create(
    username='vendor1',
    defaults={'email': 'vendor@example.com'}
)
if created:
    vendor_user.set_password('vendor123')
    vendor_user.save()
    vendor_profile, _ = UserProfile.objects.get_or_create(
        user=vendor_user,
        defaults={'role': 'vendor', 'phone_number': '+201234567890'}
    )
    print("✅ تم إنشاء Vendor")
else:
    vendor_profile = vendor_user.userprofile

# إنشاء Category
category, created = Category.objects.get_or_create(
    slug='medical-equipment',
    defaults={
        'name': 'أجهزة طبية',
        'description': 'أجهزة العلاج الطبيعي والأجهزة الطبية'
    }
)
if created:
    print("✅ تم إنشاء Category")

# إنشاء Product
product, created = Product.objects.get_or_create(
    slug='ultrasound-machine',
    defaults={
        'vendor': vendor_profile,
        'category': category,
        'name': 'جهاز الموجات فوق الصوتية',
        'description': 'جهاز احترافي للموجات فوق الصوتية للعلاج الطبيعي',
        'short_description': 'جهاز موجات فوق صوتية عالي الجودة',
        'price': 15000.00,
        'compare_at_price': 18000.00,
        'sku': 'US-001',
        'stock_quantity': 5,
        'is_active': True,
        'is_featured': True
    }
)
if created:
    print("✅ تم إنشاء Product")

# إنشاء Company
company_user, created = User.objects.get_or_create(
    username='company1',
    defaults={'email': 'company@example.com'}
)
if created:
    company_user.set_password('company123')
    company_user.save()
    company_profile, _ = UserProfile.objects.get_or_create(
        user=company_user,
        defaults={'role': 'company', 'phone_number': '+201234567891'}
    )
    print("✅ تم إنشاء Company")
else:
    company_profile = company_user.userprofile

# إنشاء Job
job, created = JobPost.objects.get_or_create(
    company=company_profile,
    title='أخصائي علاج طبيعي مطلوب',
    defaults={
        'description': 'نبحث عن أخصائي علاج طبيعي بخبرة 3 سنوات',
        'location': 'القاهرة، مصر',
        'is_full_time': True,
        'salary_range': '8000-12000 EGP'
    }
)
if created:
    print("✅ تم إنشاء Job")

# إنشاء Trainer
trainer_user, created = User.objects.get_or_create(
    username='trainer1',
    defaults={'email': 'trainer@example.com'}
)
if created:
    trainer_user.set_password('trainer123')
    trainer_user.save()
    trainer_profile, _ = UserProfile.objects.get_or_create(
        user=trainer_user,
        defaults={'role': 'trainer', 'phone_number': '+201234567892'}
    )
    print("✅ تم إنشاء Trainer")
else:
    trainer_profile = trainer_user.userprofile

# إنشاء Course
course, created = Course.objects.get_or_create(
    slug='physiotherapy-basics',
    defaults={
        'trainer': trainer_profile,
        'title': 'أساسيات العلاج الطبيعي',
        'description': 'كورس شامل في أساسيات العلاج الطبيعي',
        'short_description': 'تعلم أساسيات العلاج الطبيعي',
        'price': 500.00,
        'is_free': False,
        'duration_hours': 20,
        'level': 'beginner',
        'is_published': True
    }
)
if created:
    print("✅ تم إنشاء Course")

# إنشاء Clinic
clinic, created = Clinic.objects.get_or_create(
    slug='healthcare-plus',
    defaults={
        'company': company_profile,
        'name': 'HealthCare Plus',
        'description': 'عيادة متخصصة في العلاج الطبيعي',
        'address': 'شارع التحرير، القاهرة',
        'city': 'القاهرة',
        'phone': '+201234567893',
        'email': 'info@healthcareplus.com',
        'subscription_tier': 'professional',
        'is_active': True
    }
)
if created:
    print("✅ تم إنشاء Clinic")

# إنشاء Post
post_user = User.objects.first()
if post_user and hasattr(post_user, 'userprofile'):
    post, created = Post.objects.get_or_create(
        author=post_user.userprofile,
        content='مرحباً بكم في Phyzioline - أكبر منصة علاج طبيعي في العالم!',
        defaults={
            'category': 'general',
            'is_published': True
        }
    )
    if created:
        print("✅ تم إنشاء Post")

print("\n🎉 تم إنشاء البيانات التجريبية بنجاح!")
print("\n📝 معلومات المستخدمين:")
print("Vendor: username='vendor1', password='vendor123'")
print("Company: username='company1', password='company123'")
print("Trainer: username='trainer1', password='trainer123'")

