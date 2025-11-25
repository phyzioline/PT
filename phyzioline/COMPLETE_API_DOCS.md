# 📚 Phyzioline - Complete API Documentation
## توثيق شامل لجميع API Endpoints

---

## 🌐 Base URL
```
http://localhost:8000/api/v1/
```

---

## 🔐 Authentication Endpoints

### Register
**POST** `/api/v1/auth/register/`
- إنشاء حساب جديد
- Roles: patient, doctor, specialist, vendor, company, trainer, admin

### Login
**POST** `/api/v1/auth/login/`
- تسجيل الدخول والحصول على JWT tokens

### Logout
**POST** `/api/v1/auth/logout/`
- تسجيل الخروج (blacklist token)

### Refresh Token
**POST** `/api/v1/auth/refresh/`
- تجديد access token

---

## 👤 Accounts Endpoints

### Get My Profile
**GET** `/api/v1/accounts/profile/`
- عرض ملف التعريف الحالي

### Update Profile
**PUT/PATCH** `/api/v1/accounts/profile/`
- تحديث ملف التعريف

### Get Public Profile
**GET** `/api/v1/accounts/profile/{id}/`
- عرض ملف تعريف عام

---

## 💼 Jobs Endpoints

### Job Posts
- **GET** `/api/v1/jobs/posts/` - قائمة الوظائف
- **POST** `/api/v1/jobs/posts/` - إنشاء وظيفة (Company only)
- **GET** `/api/v1/jobs/posts/{id}/` - تفاصيل وظيفة
- **PUT/PATCH** `/api/v1/jobs/posts/{id}/` - تحديث وظيفة
- **DELETE** `/api/v1/jobs/posts/{id}/` - حذف وظيفة
- **GET** `/api/v1/jobs/posts/my_jobs/` - وظائف الشركة

### Job Applications
- **GET** `/api/v1/jobs/applications/` - قائمة الطلبات
- **POST** `/api/v1/jobs/applications/` - تقديم على وظيفة (Specialist only)
- **GET** `/api/v1/jobs/applications/{id}/` - تفاصيل طلب
- **PATCH** `/api/v1/jobs/applications/{id}/update_status/` - تحديث الحالة (Company only)
- **GET** `/api/v1/jobs/applications/my_applications/` - طلباتي

---

## 🛒 Marketplace Endpoints

### Categories
- **GET** `/api/v1/marketplace/categories/` - قائمة الفئات
- **GET** `/api/v1/marketplace/categories/{slug}/` - تفاصيل فئة
- **GET** `/api/v1/marketplace/categories/{slug}/products/` - منتجات الفئة

### Products
- **GET** `/api/v1/marketplace/products/` - قائمة المنتجات
- **POST** `/api/v1/marketplace/products/` - إنشاء منتج (Vendor only)
- **GET** `/api/v1/marketplace/products/{slug}/` - تفاصيل منتج
- **PUT/PATCH** `/api/v1/marketplace/products/{slug}/` - تحديث منتج
- **DELETE** `/api/v1/marketplace/products/{slug}/` - حذف منتج
- **GET** `/api/v1/marketplace/products/my_products/` - منتجاتي

### Cart
- **GET** `/api/v1/marketplace/cart/` - عرض السلة
- **POST** `/api/v1/marketplace/cart/add-item/` - إضافة منتج
- **POST** `/api/v1/marketplace/cart/update-item/` - تحديث كمية
- **POST** `/api/v1/marketplace/cart/remove-item/` - حذف منتج
- **POST** `/api/v1/marketplace/cart/clear/` - تفريغ السلة

### Orders
- **GET** `/api/v1/marketplace/orders/` - قائمة الطلبات
- **POST** `/api/v1/marketplace/orders/checkout/` - إنشاء طلب من السلة
- **GET** `/api/v1/marketplace/orders/{id}/` - تفاصيل طلب

### Reviews
- **GET** `/api/v1/marketplace/reviews/` - قائمة المراجعات
- **POST** `/api/v1/marketplace/reviews/` - إنشاء مراجعة

---

## 📚 Courses Endpoints

### Courses
- **GET** `/api/v1/courses/courses/` - قائمة الكورسات
- **POST** `/api/v1/courses/courses/` - إنشاء كورس (Trainer only)
- **GET** `/api/v1/courses/courses/{slug}/` - تفاصيل كورس
- **PUT/PATCH** `/api/v1/courses/courses/{slug}/` - تحديث كورس
- **DELETE** `/api/v1/courses/courses/{slug}/` - حذف كورس
- **GET** `/api/v1/courses/courses/my_courses/` - كورساتي
- **POST** `/api/v1/courses/courses/{slug}/enroll/` - التسجيل في كورس

### Enrollments
- **GET** `/api/v1/courses/enrollments/` - تسجيلاتي
- **GET** `/api/v1/courses/enrollments/{id}/` - تفاصيل تسجيل
- **PATCH** `/api/v1/courses/enrollments/{id}/update_progress/` - تحديث التقدم

### Reviews
- **GET** `/api/v1/courses/reviews/` - تقييمات الكورسات
- **POST** `/api/v1/courses/reviews/` - إنشاء تقييم

---

## 🏥 Clinics Endpoints

### Clinics
- **GET** `/api/v1/clinics/clinics/` - قائمة العيادات
- **POST** `/api/v1/clinics/clinics/` - إنشاء عيادة (Company only)
- **GET** `/api/v1/clinics/clinics/{slug}/` - تفاصيل عيادة
- **PUT/PATCH** `/api/v1/clinics/clinics/{slug}/` - تحديث عيادة
- **DELETE** `/api/v1/clinics/clinics/{slug}/` - حذف عيادة

### Patients
- **GET** `/api/v1/clinics/patients/` - قائمة المرضى
- **POST** `/api/v1/clinics/patients/` - إضافة مريض
- **GET** `/api/v1/clinics/patients/{id}/` - تفاصيل مريض
- **PUT/PATCH** `/api/v1/clinics/patients/{id}/` - تحديث مريض

### Appointments
- **GET** `/api/v1/clinics/appointments/` - قائمة المواعيد
- **POST** `/api/v1/clinics/appointments/` - إنشاء موعد
- **GET** `/api/v1/clinics/appointments/{id}/` - تفاصيل موعد
- **PUT/PATCH** `/api/v1/clinics/appointments/{id}/` - تحديث موعد

### Medical Notes
- **GET** `/api/v1/clinics/medical-notes/` - قائمة الملاحظات
- **POST** `/api/v1/clinics/medical-notes/` - إنشاء ملاحظة (Doctor only)
- **GET** `/api/v1/clinics/medical-notes/{id}/` - تفاصيل ملاحظة

### Invoices
- **GET** `/api/v1/clinics/invoices/` - قائمة الفواتير
- **POST** `/api/v1/clinics/invoices/` - إنشاء فاتورة
- **GET** `/api/v1/clinics/invoices/{id}/` - تفاصيل فاتورة

---

## 🏠 Home Sessions Endpoints

### Availabilities
- **GET** `/api/v1/sessions/availabilities/` - قائمة التوفر
- **POST** `/api/v1/sessions/availabilities/` - إضافة توفر (Specialist only)
- **GET** `/api/v1/sessions/availabilities/nearby/` - أخصائيين قريبين

### Sessions
- **GET** `/api/v1/sessions/sessions/` - قائمة الجلسات
- **POST** `/api/v1/sessions/sessions/` - حجز جلسة (Patient only)
- **GET** `/api/v1/sessions/sessions/{id}/` - تفاصيل جلسة
- **PUT/PATCH** `/api/v1/sessions/sessions/{id}/` - تحديث جلسة

### Reviews
- **GET** `/api/v1/sessions/reviews/` - تقييمات الجلسات
- **POST** `/api/v1/sessions/reviews/` - إنشاء تقييم

---

## 📱 Feed Endpoints

### Posts
- **GET** `/api/v1/feed/posts/` - قائمة المنشورات
- **POST** `/api/v1/feed/posts/` - إنشاء منشور
- **GET** `/api/v1/feed/posts/{id}/` - تفاصيل منشور
- **PUT/PATCH** `/api/v1/feed/posts/{id}/` - تحديث منشور
- **DELETE** `/api/v1/feed/posts/{id}/` - حذف منشور
- **POST** `/api/v1/feed/posts/{id}/like/` - إعجاب/إلغاء إعجاب
- **GET** `/api/v1/feed/posts/feed/` - Feed المستخدم

### Comments
- **GET** `/api/v1/feed/comments/` - قائمة التعليقات
- **POST** `/api/v1/feed/comments/` - إنشاء تعليق
- **POST** `/api/v1/feed/comments/{id}/like/` - إعجاب تعليق

### Follows
- **GET** `/api/v1/feed/follows/` - قائمة المتابعات
- **POST** `/api/v1/feed/follows/` - متابعة مستخدم
- **POST** `/api/v1/feed/follows/toggle/` - تبديل المتابعة

---

## 📢 Ads Endpoints

### Campaigns
- **GET** `/api/v1/ads/campaigns/` - قائمة الحملات
- **POST** `/api/v1/ads/campaigns/` - إنشاء حملة
- **GET** `/api/v1/ads/campaigns/{id}/` - تفاصيل حملة
- **PUT/PATCH** `/api/v1/ads/campaigns/{id}/` - تحديث حملة

### Ads
- **GET** `/api/v1/ads/ads/` - قائمة الإعلانات
- **POST** `/api/v1/ads/ads/{id}/track_click/` - تتبع نقرة
- **POST** `/api/v1/ads/ads/{id}/track_impression/` - تتبع مشاهدة

### Analytics
- **GET** `/api/v1/ads/analytics/` - تحليلات الإعلانات

---

## 🤖 AI Engine Endpoints

### Exercises
- **GET** `/api/v1/ai/exercises/` - قائمة التمارين
- **GET** `/api/v1/ai/exercises/{id}/` - تفاصيل تمرين

### Treatment Plans
- **GET** `/api/v1/ai/treatment-plans/` - قائمة خطط العلاج
- **POST** `/api/v1/ai/treatment-plans/` - إنشاء خطة
- **POST** `/api/v1/ai/treatment-plans/generate/` - توليد خطة بالذكاء الاصطناعي

### Search
- **POST** `/api/v1/ai/search/search/` - بحث ذكي

---

## 📞 CRM Endpoints

### Contacts
- **GET** `/api/v1/crm/contacts/` - قائمة جهات الاتصال
- **POST** `/api/v1/crm/contacts/` - إضافة جهة اتصال
- **GET** `/api/v1/crm/contacts/{id}/` - تفاصيل جهة اتصال
- **PUT/PATCH** `/api/v1/crm/contacts/{id}/` - تحديث جهة اتصال

### Messages
- **GET** `/api/v1/crm/messages/` - قائمة الرسائل
- **POST** `/api/v1/crm/messages/` - إرسال رسالة
- **POST** `/api/v1/crm/messages/whatsapp-webhook/` - Webhook لـ WhatsApp

### Campaigns
- **GET** `/api/v1/crm/campaigns/` - قائمة الحملات
- **POST** `/api/v1/crm/campaigns/` - إنشاء حملة
- **POST** `/api/v1/crm/campaigns/{id}/send/` - إرسال حملة

---

## 📊 Summary

**Total API Endpoints: 100+**

- Authentication: 4 endpoints
- Accounts: 3 endpoints
- Jobs: 10+ endpoints
- Marketplace: 20+ endpoints
- Courses: 10+ endpoints
- Clinics: 15+ endpoints
- Home Sessions: 8+ endpoints
- Feed: 10+ endpoints
- Ads: 8+ endpoints
- AI Engine: 5+ endpoints
- CRM: 8+ endpoints

---

**Last Updated:** 2025-01-27

