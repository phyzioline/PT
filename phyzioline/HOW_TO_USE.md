# 🚀 Phyzioline - كيفية الاستخدام
## دليل سريع للبدء

---

## ✅ معلومات تسجيل الدخول للـ Admin

**URL:** `http://localhost:8000/admin/`

**Username:** `admin`  
**Password:** `admin123`

---

## 🔧 تشغيل السيرفر

### 1. تفعيل البيئة الافتراضية
```bash
# Windows
.\env\Scripts\activate

# Linux/Mac
source env/bin/activate
```

### 2. تشغيل السيرفر
```bash
python manage.py runserver
```

**السيرفر سيعمل على:** `http://localhost:8000`

---

## 🧪 اختبار API

### باستخدام Postman/Thunder Client:

#### 1. Register (التسجيل)
```
POST http://localhost:8000/api/v1/auth/register/
Content-Type: application/json

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "testpass123",
  "password2": "testpass123",
  "role": "doctor"
}
```

#### 2. Login (تسجيل الدخول)
```
POST http://localhost:8000/api/v1/auth/login/
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

#### 3. Get Profile (بعد Login)
```
GET http://localhost:8000/api/v1/accounts/profile/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## 📍 جميع API Endpoints

### Authentication
- `POST /api/v1/auth/register/` - التسجيل
- `POST /api/v1/auth/login/` - تسجيل الدخول
- `POST /api/v1/auth/logout/` - تسجيل الخروج
- `POST /api/v1/auth/refresh/` - تجديد Token

### Accounts
- `GET /api/v1/accounts/profile/` - ملف التعريف
- `PUT /api/v1/accounts/profile/` - تحديث الملف

### Jobs
- `GET /api/v1/jobs/posts/` - قائمة الوظائف
- `POST /api/v1/jobs/posts/` - إنشاء وظيفة

### Marketplace
- `GET /api/v1/marketplace/products/` - المنتجات
- `GET /api/v1/marketplace/cart/` - السلة

### Courses
- `GET /api/v1/courses/courses/` - الكورسات

### Clinics
- `GET /api/v1/clinics/clinics/` - العيادات

### Sessions
- `GET /api/v1/sessions/availabilities/` - توفر الأخصائيين

### Feed
- `GET /api/v1/feed/posts/` - المنشورات

### Ads
- `GET /api/v1/ads/ads/` - الإعلانات

### AI
- `GET /api/v1/ai/exercises/` - التمارين

### CRM
- `GET /api/v1/crm/contacts/` - جهات الاتصال

---

## ⚠️ استكشاف الأخطاء

### المشكلة: السيرفر لا يعمل
**الحل:**
1. تأكد من تفعيل البيئة الافتراضية
2. تأكد من تطبيق migrations: `python manage.py migrate`
3. تحقق من الأخطاء في Terminal

### المشكلة: Admin Panel لا يعمل
**الحل:**
- استخدم: Username: `admin`, Password: `admin123`
- أو أنشئ superuser جديد: `python create_superuser.py`

### المشكلة: API لا يعمل
**الحل:**
1. تأكد من أن السيرفر يعمل
2. تحقق من URL: `http://localhost:8000/api/v1/`
3. استخدم Postman أو Thunder Client للاختبار

---

## 📚 للمزيد من المعلومات

- **COMPLETE_API_DOCS.md** - توثيق شامل
- **API_USAGE.md** - دليل استخدام API
- **README.md** - دليل المشروع

---

**Last Updated:** 2025-01-27

