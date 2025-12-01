# 🏥 Phyzioline - Physical Therapy Ecosystem Platform
## أكبر منصة متكاملة للعلاج الطبيعي في العالم

> **🎉 PROJECT CLEANED & SIMPLIFIED!** This version has been optimized for easy setup and development.

---

## 🚀 QUICK START (للبدء السريع)

### Option 1: Using Startup Scripts (Easiest!)

**Step 1:** Double-click `start_backend.bat` ➜ Backend runs on http://localhost:8000

**Step 2:** Double-click `start_frontend.bat` ➜ Frontend runs on http://localhost:5173

### Option 2: Manual Start

**Backend (Django):**
```bash
cd "d:\phyzio app 2.0\phyzioline"
.\env\Scripts\activate
python manage.py runserver
```

**Frontend (React):**
```bash
cd "d:\phyzio app 2.0\phyzioline\frontend"
npm install
npm run dev
```

📖 **For detailed instructions, see [`START_HERE.md`](START_HERE.md)**

---

## 🌟 What is Phyzioline?

**Phyzioline** is an all-in-one ecosystem for the physical therapy industry with **6 core modules**:

### 🛍️ 1. Multi-Vendor Marketplace
- Amazon-style marketplace for PT equipment and medical supplies
- Vendor registration, inventory management, and payments
- Product reviews and ratings

### 🏥 2. Home Visit Booking System  
- Vezeeta-like platform for home physiotherapy sessions
- Therapist profiles, availability, and pricing
- Patient booking, payment, and reviews

### 🏢 3. Clinic ERP System
- WebPT-style clinic management
- Patient EMR, treatment plans, billing
- Insurance support and staff management

### 🎓 4. Learning & Courses Platform
- Coursera-style online courses
- Video lessons, quizzes, and certificates
- Instructor and student dashboards

### 📊 5. Global Physio Data Hub
- Worldwide physiotherapy statistics
- Salary data by country
- Licensing and immigration requirements

### 📢 6. CRM & Advertising System
- Internal ad management
- User segmentation and analytics
- Lead tracking and automation

---

## 🛠️ Tech Stack

### ⚙️ Backend
- **Django 5.2.8** - Main framework
- **Django REST Framework** - API layer
- **JWT Authentication** - Secure auth
- **SQLite** (dev) / **PostgreSQL** (prod)

### 💻 Frontend  
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **React Router** - Navigation

---

## 📁 Cleaned Project Structure

```
phyzioline/
│
├── 📜 START_HERE.md              ⭐ Start here for setup guide
├── 🚀 start_backend.bat          ⭐ Run Django with one click
├── 🚀 start_frontend.bat         ⭐ Run React with one click
│
├── 🔧 Backend Modules (Django Apps)
│   ├── accounts/                 User auth & profiles
│   ├── marketplace/              E-commerce system
│   ├── courses/                  Learning platform
│   ├── clinics/                  Clinic ERP
│   ├── home_sessions/            Home visit bookings
│   ├── jobs/                     Job posting system
│   ├── feed/                     Social feed
│   ├── crm/                      CRM system
│   ├── ads/                      Advertisement
│   ├── ai_engine/                AI recommendations
│   ├── global_stats/             Global PT data
│   └── equivalency/              License equivalency
│
├── 💻 Frontend (React + TypeScript)
│   └── frontend/                 Modern React app
│
└── 📚 Documentation
    ├── API_ENDPOINTS.md          Complete API docs
    ├── QUICK_START.md            Detailed setup
    └── HOW_TO_USE.md             Usage guide
```

---

## 🔌 Main API Endpoints

**Base URL:** `http://localhost:8000/api/v1/`

| Module | Endpoint | Description |
|--------|----------|-------------|
| **Auth** | `POST /auth/register/` | Register new user |
| | `POST /auth/login/` | User login |
| **Feed** | `GET /feed/posts/` | Get feed posts |
| **Marketplace** | `GET /marketplace/products/` | List products |
| | `POST /marketplace/orders/checkout/` | Create order |
| **Courses** | `GET /courses/` | List courses |
| | `POST /courses/{id}/enroll/` | Enroll in course |
| **Jobs** | `GET /jobs/posts/` | List job postings |
| | `POST /jobs/apply/` | Apply to job |
| **Sessions** | `GET /home-sessions/therapists/` | List therapists |
| | `POST /home-sessions/book/` | Book session |

📖 **See [`API_ENDPOINTS.md`](API_ENDPOINTS.md) for complete documentation**

---

## 👥 User Roles

The platform supports **7 user roles**:

1. **Patient** - Book sessions, buy products, enroll in courses
2. **Therapist** - Offer home visits, manage bookings
3. **Clinic Owner** - Manage clinic, staff, and patients
4. **Vendor** - Sell products on marketplace
5. **Instructor** - Create and sell courses
6. **Student** - Take courses and earn certificates
7. **Admin** - Full system access and management

---

## ✅ What Was Cleaned

**❌ Removed (unnecessary files):**
- `phyzioline static html/` - Old downloaded files
- `frontend_static/` - Outdated static HTML
- `frontend-react/` - Old React version
- `Node.js/` and `node/` - Duplicate folders

**✅ Kept (essential files):**
- Django backend with all 12 modules
- Modern React + TypeScript frontend
- Core documentation files
- Startup scripts for easy development

---

## 🎯 Current Status

| Module | Backend API | Frontend | Status |
|--------|------------|----------|--------|
| Authentication | ✅ | ✅ | Complete |
| Feed | ✅ | 🚧 | API Ready |
| Marketplace | ✅ | 🚧 | API Ready |
| Courses | ✅ | 🚧 | API Ready |
| Home Sessions | ✅ | 🚧 | API Ready |
| Jobs | ✅ | 🚧 | API Ready |
| Clinic ERP | ✅ | 🚧 | API Ready |
| CRM | ✅ | 🚧 | API Ready |
| Ads | ✅ | 🚧 | API Ready |
| AI Engine | ✅ | 🚧 | API Ready |

---

## 🐛 Troubleshooting

### Backend Issues
```bash
# Activate environment
.\env\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate
```

### Frontend Issues  
```bash
cd frontend
Remove-Item node_modules -Recurse
npm install
npm run dev
```

---

## 📚 Documentation Files

- **[START_HERE.md](START_HERE.md)** ⭐ - Quick start guide
- **[QUICK_START.md](QUICK_START.md)** - Detailed setup
- **[API_ENDPOINTS.md](API_ENDPOINTS.md)** - Complete API reference
- **[HOW_TO_USE.md](HOW_TO_USE.md)** - Usage guide
- **[ADMIN_CREDENTIALS.md](ADMIN_CREDENTIALS.md)** - Admin access

---

## 🎉 Ready to Build!

Your project is now **clean, organized, and ready to run**!

**Next steps:**
1. Run `start_backend.bat` (or use manual commands)
2. Run `start_frontend.bat` (or use manual commands)
3. Open http://localhost:5173 in your browser
4. Start developing your modules! 🚀

---

## 📄 License

MIT License

---

**Made with ❤️ for Physiotherapy Professionals Worldwide**

