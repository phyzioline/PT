# 🏥 Phyzioline - أكبر منصة علاج طبيعي في العالم
## The World's Largest Physiotherapy Platform

---

## 🌟 نظرة عامة

**Phyzioline** هو Super Platform متكامل يشمل 10 خدمات رئيسية في مكان واحد:

1. **Marketplace** - أجهزة علاج طبيعي
2. **Courses Platform** - كورسات وتأهيل
3. **Jobs System** - نظام توظيف
4. **Clinic Management** - نظام إدارة عيادات (SaaS)
5. **Private Sessions** - جلسات منزلية (Uber-like)
6. **Clinic Rental** - تأجير عيادات
7. **CRM + WhatsApp** - إدارة علاقات العملاء
8. **AI Treatment Engine** - محرك ذكي للعلاج
9. **Social Feed** - نظام Feed اجتماعي
10. **Ads Center** - مركز الإعلانات

---

## 🛠️ التقنيات المستخدمة

### Backend
- **Django 5.2.8** - Framework الرئيسي
- **Django REST Framework** - API
- **JWT Authentication** - المصادقة
- **PostgreSQL** - قاعدة البيانات (Production)
- **SQLite** - قاعدة البيانات (Development)

### Frontend (قريباً)
- **Next.js** - React Framework
- **TailwindCSS** - Styling
- **Zustand/Redux** - State Management

---

## 📦 التثبيت

### 1. Clone المشروع
```bash
git clone <repository-url>
cd phyzioline
```

### 2. إنشاء Virtual Environment
```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python3 -m venv env
source env/bin/activate
```

### 3. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

### 4. تشغيل Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. إنشاء Superuser
```bash
python manage.py createsuperuser
```

### 6. تشغيل السيرفر
```bash
python manage.py runserver
```

---

## 📚 التوثيق

- **API Usage:** `API_USAGE.md`
- **Architecture:** `ARCHITECTURE_PLAN.md`
- **Quick Start:** `QUICK_START.md`
- **Deployment:** `DEPLOYMENT.md`
- **Project Status:** `PROJECT_STATUS.md`

---

## 🔌 API Endpoints

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
- `GET /api/v1/jobs/applications/` - طلبات التقديم

### Marketplace
- `GET /api/v1/marketplace/products/` - المنتجات
- `GET /api/v1/marketplace/cart/` - السلة
- `POST /api/v1/marketplace/orders/checkout/` - إنشاء طلب

---

## 🏗️ هيكل المشروع

```
phyzioline/
├── phyzioline_core/      # Main Django project
├── core_data/            # Shared utilities
├── accounts/             # Authentication
├── jobs/                 # Jobs system
├── marketplace/          # E-commerce
├── courses/              # Courses platform
├── clinics/             # Clinic management
├── sessions/             # Private sessions
├── feed/                 # Social feed
├── ads/                  # Ads center
├── ai_engine/            # AI engine
└── crm/                  # CRM system
```

---

## ✅ الحالة الحالية

- ✅ Phase 1: Core System
- ✅ Phase 2: Marketplace
- ✅ Phase 3: Jobs System
- ⏳ Phase 4-10: قيد التطوير

---

## 🤝 المساهمة

المشروع قيد التطوير النشط. للمساهمة:

1. Fork المشروع
2. إنشاء branch جديد
3. Commit التغييرات
4. Push إلى branch
5. إنشاء Pull Request

---

## 📄 الرخصة

MIT License

---

## 📞 التواصل

للمزيد من المعلومات، راجع ملفات التوثيق في المشروع.

---

**Made with ❤️ for Physiotherapy Professionals Worldwide**

