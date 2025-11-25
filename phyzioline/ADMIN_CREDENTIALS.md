# 🔐 Admin Panel - معلومات تسجيل الدخول

## معلومات Superuser

**Username:** `admin`  
**Password:** `admin123`  
**Email:** `admin@phyzioline.com`

---

## كيفية تسجيل الدخول

1. افتح المتصفح
2. اذهب إلى: `http://localhost:8000/admin/`
3. أدخل:
   - Username: `admin`
   - Password: `admin123`
4. اضغط Login

---

## إنشاء مستخدم جديد

إذا أردت إنشاء مستخدم جديد:

```bash
python manage.py createsuperuser
```

أو استخدم:

```bash
python create_superuser.py
```

---

## ملاحظات

- تأكد من أن السيرفر يعمل: `python manage.py runserver`
- إذا لم يعمل، تحقق من الأخطاء في Terminal
- تأكد من تطبيق migrations: `python manage.py migrate`

---

**Last Updated:** 2025-01-27

