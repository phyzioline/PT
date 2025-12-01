# Phyzioline API - All Module Endpoints

**Base URL:** `http://localhost:8000/api/v1/`

---

## 📋 API Root
- **GET** `/api/v1/` - API Root (قائمة بجميع الوحدات)

---

## 🔐 1. Authentication Module

### Base: `/api/v1/auth/`

- **POST** `/api/v1/auth/register/` - تسجيل مستخدم جديد
- **POST** `/api/v1/auth/login/` - تسجيل الدخول (الحصول على JWT Token)
- **POST** `/api/v1/auth/logout/` - تسجيل الخروج
- **POST** `/api/v1/auth/refresh/` - تحديث JWT Token

### Profile Endpoints

- **GET** `/api/v1/profile/` - عرض ملف التعريف الحالي (يتطلب تسجيل دخول)
- **PUT** `/api/v1/profile/` - تحديث ملف التعريف
- **PATCH** `/api/v1/profile/` - تحديث جزئي لملف التعريف
- **GET** `/api/v1/profile/<id>/` - عرض ملف تعريف عام (public)

---

## 🛒 2. Marketplace Module

### Base: `/api/v1/marketplace/`

### Products
- **GET** `/api/v1/marketplace/products/` - قائمة المنتجات
- **POST** `/api/v1/marketplace/products/` - إنشاء منتج جديد (Vendor)
- **GET** `/api/v1/marketplace/products/<id>/` - تفاصيل منتج
- **PUT** `/api/v1/marketplace/products/<id>/` - تحديث منتج
- **DELETE** `/api/v1/marketplace/products/<id>/` - حذف منتج

### Categories
- **GET** `/api/v1/marketplace/categories/` - قائمة الفئات
- **POST** `/api/v1/marketplace/categories/` - إنشاء فئة جديدة (Admin)
- **GET** `/api/v1/marketplace/categories/<id>/` - تفاصيل فئة
- **PUT** `/api/v1/marketplace/categories/<id>/` - تحديث فئة
- **DELETE** `/api/v1/marketplace/categories/<id>/` - حذف فئة

### Cart
- **GET** `/api/v1/marketplace/cart/` - عرض السلة (يتطلب تسجيل دخول)
- **POST** `/api/v1/marketplace/cart/add/` - إضافة منتج للسلة
- **PUT** `/api/v1/marketplace/cart/update/<id>/` - تحديث كمية منتج
- **DELETE** `/api/v1/marketplace/cart/remove/<id>/` - حذف منتج من السلة
- **POST** `/api/v1/marketplace/cart/clear/` - تفريغ السلة

### Orders
- **GET** `/api/v1/marketplace/orders/` - قائمة الطلبات
- **POST** `/api/v1/marketplace/orders/` - إنشاء طلب جديد
- **GET** `/api/v1/marketplace/orders/<id>/` - تفاصيل طلب
- **PUT** `/api/v1/marketplace/orders/<id>/cancel/` - إلغاء طلب

### Reviews
- **GET** `/api/v1/marketplace/reviews/` - قائمة التقييمات
- **POST** `/api/v1/marketplace/reviews/` - إضافة تقييم
- **GET** `/api/v1/marketplace/reviews/<id>/` - تفاصيل تقييم

---

## 💼 3. Jobs Module

### Base: `/api/v1/jobs/`

### Job Posts
- **GET** `/api/v1/jobs/posts/` - قائمة الوظائف
- **POST** `/api/v1/jobs/posts/` - إنشاء وظيفة جديدة (Company)
- **GET** `/api/v1/jobs/posts/<id>/` - تفاصيل وظيفة
- **PUT** `/api/v1/jobs/posts/<id>/` - تحديث وظيفة
- **DELETE** `/api/v1/jobs/posts/<id>/` - حذف وظيفة

### Job Applications
- **GET** `/api/v1/jobs/applications/` - قائمة التقديمات
- **POST** `/api/v1/jobs/applications/` - تقديم على وظيفة
- **GET** `/api/v1/jobs/applications/<id>/` - تفاصيل تقديم
- **PUT** `/api/v1/jobs/applications/<id>/status/` - تحديث حالة التقديم

---

## 📚 4. Courses Module

### Base: `/api/v1/courses/`

### Courses
- **GET** `/api/v1/courses/courses/` - قائمة الكورسات
- **POST** `/api/v1/courses/courses/` - إنشاء كورس جديد (Trainer)
- **GET** `/api/v1/courses/courses/<id>/` - تفاصيل كورس
- **PUT** `/api/v1/courses/courses/<id>/` - تحديث كورس
- **DELETE** `/api/v1/courses/courses/<id>/` - حذف كورس

### Lessons
- **GET** `/api/v1/courses/lessons/` - قائمة الدروس
- **POST** `/api/v1/courses/lessons/` - إنشاء درس جديد
- **GET** `/api/v1/courses/lessons/<id>/` - تفاصيل درس
- **PUT** `/api/v1/courses/lessons/<id>/` - تحديث درس

### Enrollments
- **GET** `/api/v1/courses/enrollments/` - قائمة التسجيلات
- **POST** `/api/v1/courses/enrollments/` - التسجيل في كورس
- **GET** `/api/v1/courses/enrollments/<id>/` - تفاصيل تسجيل

### Certificates
- **GET** `/api/v1/courses/certificates/` - قائمة الشهادات
- **GET** `/api/v1/courses/certificates/<id>/` - تفاصيل شهادة

---

## 🏥 5. Clinics Module

### Base: `/api/v1/clinics/`

### Clinics
- **GET** `/api/v1/clinics/clinics/` - قائمة العيادات (Company only)
- **POST** `/api/v1/clinics/clinics/` - إنشاء عيادة جديدة
- **GET** `/api/v1/clinics/clinics/<slug>/` - تفاصيل عيادة
- **PUT** `/api/v1/clinics/clinics/<slug>/` - تحديث عيادة
- **DELETE** `/api/v1/clinics/clinics/<slug>/` - حذف عيادة

### Patients
- **GET** `/api/v1/clinics/patients/` - قائمة المرضى
- **POST** `/api/v1/clinics/patients/` - إضافة مريض جديد
- **GET** `/api/v1/clinics/patients/<id>/` - تفاصيل مريض
- **PUT** `/api/v1/clinics/patients/<id>/` - تحديث بيانات مريض

### Appointments
- **GET** `/api/v1/clinics/appointments/` - قائمة المواعيد
- **POST** `/api/v1/clinics/appointments/` - حجز موعد جديد
- **GET** `/api/v1/clinics/appointments/<id>/` - تفاصيل موعد
- **PUT** `/api/v1/clinics/appointments/<id>/` - تحديث موعد
- **PUT** `/api/v1/clinics/appointments/<id>/cancel/` - إلغاء موعد

### Medical Notes
- **GET** `/api/v1/clinics/medical-notes/` - قائمة الملاحظات الطبية
- **POST** `/api/v1/clinics/medical-notes/` - إضافة ملاحظة طبية
- **GET** `/api/v1/clinics/medical-notes/<id>/` - تفاصيل ملاحظة

### Invoices
- **GET** `/api/v1/clinics/invoices/` - قائمة الفواتير
- **POST** `/api/v1/clinics/invoices/` - إنشاء فاتورة
- **GET** `/api/v1/clinics/invoices/<id>/` - تفاصيل فاتورة

---

## 🏠 6. Home Sessions Module

### Base: `/api/v1/sessions/`

### Sessions
- **GET** `/api/v1/sessions/sessions/` - قائمة الجلسات (Specialist only)
- **POST** `/api/v1/sessions/sessions/` - إنشاء جلسة جديدة
- **GET** `/api/v1/sessions/sessions/<id>/` - تفاصيل جلسة
- **PUT** `/api/v1/sessions/sessions/<id>/` - تحديث جلسة
- **PUT** `/api/v1/sessions/sessions/<id>/complete/` - إكمال جلسة

### Specialist Availability
- **GET** `/api/v1/sessions/availability/` - قائمة أوقات التوفر
- **POST** `/api/v1/sessions/availability/` - إضافة وقت توفر
- **GET** `/api/v1/sessions/availability/<id>/` - تفاصيل وقت توفر
- **PUT** `/api/v1/sessions/availability/<id>/` - تحديث وقت توفر

### Session Reviews
- **GET** `/api/v1/sessions/reviews/` - قائمة تقييمات الجلسات
- **POST** `/api/v1/sessions/reviews/` - إضافة تقييم

---

## 📱 7. Social Feed Module

### Base: `/api/v1/feed/`

### Posts
- **GET** `/api/v1/feed/posts/` - قائمة المنشورات
- **POST** `/api/v1/feed/posts/` - إنشاء منشور جديد
- **GET** `/api/v1/feed/posts/<id>/` - تفاصيل منشور
- **PUT** `/api/v1/feed/posts/<id>/` - تحديث منشور
- **DELETE** `/api/v1/feed/posts/<id>/` - حذف منشور

### Comments
- **GET** `/api/v1/feed/comments/` - قائمة التعليقات
- **POST** `/api/v1/feed/comments/` - إضافة تعليق
- **GET** `/api/v1/feed/comments/<id>/` - تفاصيل تعليق
- **PUT** `/api/v1/feed/comments/<id>/` - تحديث تعليق
- **DELETE** `/api/v1/feed/comments/<id>/` - حذف تعليق

### Likes
- **POST** `/api/v1/feed/posts/<id>/like/` - إعجاب بمنشور
- **DELETE** `/api/v1/feed/posts/<id>/like/` - إلغاء إعجاب
- **POST** `/api/v1/feed/comments/<id>/like/` - إعجاب بتعليق

### Follow
- **POST** `/api/v1/feed/follow/<user_id>/` - متابعة مستخدم
- **DELETE** `/api/v1/feed/follow/<user_id>/` - إلغاء متابعة
- **GET** `/api/v1/feed/followers/` - قائمة المتابعين
- **GET** `/api/v1/feed/following/` - قائمة المتابَعين

---

## 📢 8. Ads Module

### Base: `/api/v1/ads/`

### Campaigns
- **GET** `/api/v1/ads/campaigns/` - قائمة الحملات (يتطلب تسجيل دخول)
- **POST** `/api/v1/ads/campaigns/` - إنشاء حملة جديدة
- **GET** `/api/v1/ads/campaigns/<id>/` - تفاصيل حملة
- **PUT** `/api/v1/ads/campaigns/<id>/` - تحديث حملة
- **DELETE** `/api/v1/ads/campaigns/<id>/` - حذف حملة

### Ads
- **GET** `/api/v1/ads/ads/` - قائمة الإعلانات
- **POST** `/api/v1/ads/ads/` - إنشاء إعلان جديد
- **GET** `/api/v1/ads/ads/<id>/` - تفاصيل إعلان
- **PUT** `/api/v1/ads/ads/<id>/` - تحديث إعلان

### Analytics
- **GET** `/api/v1/ads/analytics/` - إحصائيات الإعلانات
- **GET** `/api/v1/ads/campaigns/<id>/analytics/` - إحصائيات حملة

---

## 🤖 9. AI Engine Module

### Base: `/api/v1/ai/`

### Exercises
- **GET** `/api/v1/ai/exercises/` - قائمة التمارين
- **POST** `/api/v1/ai/exercises/` - إضافة تمرين جديد
- **GET** `/api/v1/ai/exercises/<id>/` - تفاصيل تمرين
- **PUT** `/api/v1/ai/exercises/<id>/` - تحديث تمرين

### Treatment Plans
- **GET** `/api/v1/ai/treatment-plans/` - قائمة خطط العلاج
- **POST** `/api/v1/ai/treatment-plans/` - إنشاء خطة علاج
- **GET** `/api/v1/ai/treatment-plans/<id>/` - تفاصيل خطة علاج

### Search
- **POST** `/api/v1/ai/search/` - البحث في قاعدة التمارين
- **GET** `/api/v1/ai/search-logs/` - سجل عمليات البحث

---

## 📞 10. CRM Module

### Base: `/api/v1/crm/`

### Campaigns
- **GET** `/api/v1/crm/campaigns/` - قائمة حملات CRM
- **POST** `/api/v1/crm/campaigns/` - إنشاء حملة جديدة
- **GET** `/api/v1/crm/campaigns/<id>/` - تفاصيل حملة
- **PUT** `/api/v1/crm/campaigns/<id>/` - تحديث حملة

### Contacts
- **GET** `/api/v1/crm/contacts/` - قائمة جهات الاتصال
- **POST** `/api/v1/crm/contacts/` - إضافة جهة اتصال
- **GET** `/api/v1/crm/contacts/<id>/` - تفاصيل جهة اتصال
- **PUT** `/api/v1/crm/contacts/<id>/` - تحديث جهة اتصال

### Messages
- **GET** `/api/v1/crm/messages/` - قائمة الرسائل
- **POST** `/api/v1/crm/messages/` - إرسال رسالة
- **GET** `/api/v1/crm/messages/<id>/` - تفاصيل رسالة

---

## 🌍 11. Equivalency Module

### Base: `/api/v1/equivalency/`

### Countries
- **GET** `/api/v1/equivalency/countries/` - قائمة الدول
- **GET** `/api/v1/equivalency/countries/<id>/` - تفاصيل دولة

### Requirements
- **GET** `/api/v1/equivalency/requirements/` - قائمة المتطلبات
- **GET** `/api/v1/equivalency/requirements/<id>/` - تفاصيل متطلبات
- **GET** `/api/v1/equivalency/requirements/?country=<code>` - متطلبات دولة محددة

### Documents
- **GET** `/api/v1/equivalency/documents/` - قائمة المستندات المطلوبة
- **GET** `/api/v1/equivalency/documents/<id>/` - تفاصيل مستند

---

## 📊 12. Global Stats Module

### Base: `/api/v1/global-stats/`

### Snapshots
- **GET** `/api/v1/global-stats/snapshots/` - قائمة لقطات البيانات
- **GET** `/api/v1/global-stats/snapshots/<id>/` - تفاصيل لقطة

### Country Stats
- **GET** `/api/v1/global-stats/countries/` - إحصائيات الدول
- **GET** `/api/v1/global-stats/countries/<id>/` - إحصائيات دولة محددة

---

## 💳 13. Payments Module

### Base: `/api/v1/payments/`

### Payment Gateways
- **GET** `/api/v1/payments/gateways/` - قائمة بوابات الدفع
- **GET** `/api/v1/payments/gateways/<id>/` - تفاصيل بوابة دفع

### Transactions
- **GET** `/api/v1/payments/transactions/` - قائمة المعاملات
- **POST** `/api/v1/payments/transactions/` - إنشاء معاملة جديدة
- **GET** `/api/v1/payments/transactions/<id>/` - تفاصيل معاملة
- **POST** `/api/v1/payments/transactions/<id>/verify/` - التحقق من معاملة

### Webhooks
- **POST** `/api/v1/payments/webhooks/paymob/` - Webhook لـ Paymob

---

## 🔧 Additional Endpoints

### JWT Token Management
- **POST** `/api/token/` - الحصول على JWT Token (Simple JWT)
- **POST** `/api/token/refresh/` - تحديث JWT Token

### Content Module
- **GET** `/api/v1/content/equivalence/` - متطلبات المعادلة
- **GET** `/api/v1/content/explore/` - بيانات الاستكشاف

### HTMX Endpoints
- **GET** `/htmx/feed/` - HTMX feed fragment

---

## 📝 Notes

- جميع الـ endpoints التي تتطلب تسجيل دخول تحتاج إلى JWT Token في Header:
  ```
  Authorization: Bearer <your_access_token>
  ```

- بعض الـ endpoints تتطلب صلاحيات محددة:
  - **Company**: للشركات فقط
  - **Doctor**: للأطباء فقط
  - **Specialist**: للأخصائيين فقط
  - **Vendor**: للتجار فقط
  - **Trainer**: للمحاضرين فقط
  - **Admin**: للمدراء فقط

- Base URL للتطوير: `http://localhost:8000`
- Base URL للإنتاج: سيتم تحديثه لاحقاً

---

**Last Updated:** 2025-11-25



