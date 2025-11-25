# 🚀 Phyzioline - Quick Start Guide

## 📋 المتطلبات (Prerequisites)

- Python 3.11+
- pip
- Virtual environment (موصى به)

---

## ⚙️ الإعداد (Setup)

### 1. تفعيل البيئة الافتراضية (Virtual Environment)
```bash
# Windows
phyzioline\env\Scripts\activate

# Linux/Mac
source phyzioline/env/bin/activate
```

### 2. تثبيت المتطلبات
```bash
cd phyzioline
pip install -r requirements.txt
```

### 3. تشغيل Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. إنشاء Superuser (اختياري)
```bash
python manage.py createsuperuser
```

### 5. تشغيل السيرفر
```bash
python manage.py runserver
```

الآن السيرفر يعمل على: `http://localhost:8000`

---

## 🧪 اختبار الـ API

### باستخدام cURL:

#### 1. التسجيل (Register)
```bash
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password2": "testpass123",
    "role": "doctor"
  }'
```

#### 2. تسجيل الدخول (Login)
```bash
curl -X POST http://localhost:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

احفظ `access` token من الاستجابة.

#### 3. عرض ملف التعريف (Get Profile)
```bash
curl -X GET http://localhost:8000/api/v1/accounts/profile/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 📁 هيكل المشروع

```
phyzioline/
├── phyzioline_core/      # Main Django project
│   ├── settings.py       # ✅ تم توحيده
│   └── urls.py           # ✅ تم تحديثه
│
├── accounts/             # ✅ Authentication & User Management
│   ├── models.py        # ✅ UserProfile model
│   ├── serializers.py   # ✅ تم إنشاؤه
│   ├── views.py         # ✅ تم إنشاؤه
│   └── urls.py          # ✅ تم إنشاؤه
│
├── jobs/                # ⏳ Models موجودة، تحتاج API
├── marketplace/         # ⏳ سيتم إضافتها لاحقاً
│
└── requirements.txt     # ✅ تم إنشاؤه
```

---

## ✅ ما تم إنجازه

- [x] توحيد `settings.py` مع جميع التطبيقات
- [x] إعداد JWT Authentication
- [x] إنشاء Authentication API (register, login, logout, refresh)
- [x] إنشاء User Profile API (get, update)
- [x] إعداد CORS للسماح بالاتصال من Frontend
- [x] إضافة Media & Static files configuration
- [x] إنشاء `requirements.txt`
- [x] إنشاء توثيق API

---

## 🔜 الخطوات التالية

1. **اختبار جميع الـ endpoints** باستخدام Postman/Thunder Client
2. **إنشاء Jobs API** (Phase 3)
3. **إضافة Permissions System** (role-based permissions)
4. **بدء Marketplace implementation** (Phase 2)

---

## 📚 التوثيق

- **API Usage:** راجع `API_USAGE.md` للتفاصيل الكاملة
- **Architecture Plan:** راجع `ARCHITECTURE_PLAN.md`
- **Current Status:** راجع `CURRENT_STATUS.md`

---

## 🐛 استكشاف الأخطاء

### مشكلة: `ModuleNotFoundError: No module named 'rest_framework'`
**الحل:** قم بتثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

### مشكلة: `No such table: accounts_userprofile`
**الحل:** قم بتشغيل migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### مشكلة: CORS error في Frontend
**الحل:** تأكد من إضافة Frontend URL في `CORS_ALLOWED_ORIGINS` في `settings.py`

---

## 📞 الدعم

للمزيد من المعلومات، راجع ملفات التوثيق:
- `ARCHITECTURE_PLAN.md`
- `CURRENT_STATUS.md`
- `API_DESIGN.md`
- `API_USAGE.md`

---

**Happy Coding! 🎉**

