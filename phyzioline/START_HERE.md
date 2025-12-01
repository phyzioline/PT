# 🚀 Phyzioline - START HERE

## Quick Start Guide (للبدء السريع)

This is the **simplified** version of Phyzioline - cleaned up and ready to run!

---

## 📁 Project Structure

```
phyzioline/
├── 🔧 Backend (Django)
│   ├── accounts/          # User authentication & profiles
│   ├── marketplace/       # E-commerce system
│   ├── courses/          # Learning platform
│   ├── clinics/          # Clinic ERP
│   ├── home_sessions/    # Home visit bookings
│   ├── jobs/             # Job posting system
│   ├── feed/             # Social feed
│   ├── crm/              # CRM system
│   ├── ads/              # Advertisement system
│   ├── ai_engine/        # AI recommendations
│   ├── global_stats/     # Global physio data
│   ├── equivalency/      # License equivalency
│   └── manage.py         # Django management
│
└── 💻 Frontend (React + TypeScript)
    └── frontend/         # Modern React app with Tailwind CSS
```

---

## ⚡ How to Run (كيف تشغل المشروع)

### Step 1: Start Backend (Django)

```bash
# Navigate to project folder
cd "d:\phyzio app 2.0\phyzioline"

# Activate virtual environment
.\env\Scripts\activate

# Install dependencies (first time only)
pip install -r requirements.txt

# Run migrations (first time only)
python manage.py migrate

# Start Django server
python manage.py runserver
```

Backend will run on: **http://localhost:8000**

---

### Step 2: Start Frontend (React)

Open a **NEW terminal** window:

```bash
# Navigate to frontend folder
cd "d:\phyzio app 2.0\phyzioline\frontend"

# Install dependencies (first time only)
npm install

# Start React development server
npm run dev
```

Frontend will run on: **http://localhost:5173**

---

## 🎯 What Was Removed

✅ **Deleted unnecessary files:**
- `phyzioline static html/` - Old downloaded static files
- `frontend_static/` - Outdated static HTML
- `frontend-react/` - Older React version without TypeScript
- `Node.js/` and `node/` - Duplicate node folders

✅ **Kept:**
- Django backend with all modules
- Modern React + TypeScript + Tailwind frontend
- All essential documentation

---

## 👤 Admin Access

**Default Admin Credentials:**
- Check `ADMIN_CREDENTIALS.md` file for admin login details

Or create a new superuser:
```bash
python manage.py createsuperuser
```

---

## 📚 API Documentation

Backend API runs on: **http://localhost:8000/api/v1/**

**Key Endpoints:**
- `/api/v1/auth/register/` - Register new user
- `/api/v1/auth/login/` - Login
- `/api/v1/feed/posts/` - Get feed posts
- `/api/v1/marketplace/products/` - Get products
- `/api/v1/courses/` - Get courses
- `/api/v1/jobs/posts/` - Get job posts

See `API_ENDPOINTS.md` for complete API documentation.

---

## 🛠️ Tech Stack

**Backend:**
- Django 5.2.8
- Django REST Framework
- JWT Authentication
- SQLite (development) / PostgreSQL (production)

**Frontend:**
- React 18
- TypeScript
- Vite (build tool)
- Tailwind CSS
- React Router

---

## 🐛 Troubleshooting

### Backend won't start?
```bash
# Make sure virtual environment is activated
.\env\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate
```

### Frontend won't start?
```bash
# Delete node_modules and reinstall
cd frontend
Remove-Item node_modules -Recurse -Force
npm install
npm run dev
```

---

## 📞 Need Help?

Check these documentation files:
- `README.md` - General overview
- `QUICK_START.md` - Detailed setup guide
- `API_ENDPOINTS.md` - API documentation
- `HOW_TO_USE.md` - Usage guide

---

## 🎉 Your Project is Now Clean!

The project has been simplified to:
- ✅ One backend (Django)
- ✅ One frontend (React + TypeScript)
- ✅ Clear documentation
- ✅ Easy to run

**Next Steps:**
1. Start the backend (Step 1 above)
2. Start the frontend (Step 2 above)
3. Open http://localhost:5173 in your browser
4. Start building! 🚀

---

**Made with ❤️ for Physiotherapy Professionals Worldwide**
