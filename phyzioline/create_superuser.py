import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phyzioline_core.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile

# إنشاء superuser
username = 'admin'
email = 'admin@phyzioline.com'
password = 'admin123'

if User.objects.filter(username=username).exists():
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"تم تحديث المستخدم: {username}")
else:
    user = User.objects.create_superuser(username=username, email=email, password=password)
    print(f"تم إنشاء المستخدم: {username}")

# تحديث ملف التعريف
if hasattr(user, 'userprofile'):
    user.userprofile.role = 'admin'
    user.userprofile.save()
    print("تم تحديث الدور إلى admin")

print(f"\n✅ معلومات تسجيل الدخول:")
print(f"Username: {username}")
print(f"Password: {password}")
print(f"Email: {email}")

