# URLs & File Locations Reference

## 📍 Project Root Location
```
d:\phyzioline static html\phyzioline-ui\
```

## 🌐 URLs (After `npm run dev`)

### Homepage & Main Pages
```
http://localhost:3000/              → Homepage
http://localhost:3000/api/dashboard → Mock API endpoint
```

### Dashboard Pages
```
http://localhost:3000/dashboard/              → Redirects to overview
http://localhost:3000/dashboard/overview      → Overview page (stats, recent activity)
http://localhost:3000/dashboard/appointments  → Appointments management
http://localhost:3000/dashboard/courses       → Course progress tracking
http://localhost:3000/dashboard/profile       → User profile & preferences
```

## 📂 File Structure Reference

### Source Code Files
```
phyzioline-ui/
├── pages/
│   ├── index.jsx                      # Homepage route (/)
│   ├── _app.jsx                       # Next.js app wrapper (fonts, providers)
│   ├── api/
│   │   └── dashboard.js               # Mock API route (/api/dashboard)
│   └── dashboard/
│       ├── index.jsx                  # Dashboard index (redirects to overview)
│       ├── overview.jsx               # Overview page (/dashboard/overview)
│       ├── appointments.jsx           # Appointments page (/dashboard/appointments)
│       ├── courses.jsx                # Courses page (/dashboard/courses)
│       ├── profile.jsx                # Profile page (/dashboard/profile)
│       └── [slug].jsx                 # Dynamic dashboard routes (fallback)

├── components/
│   ├── Header.jsx                     # Navbar with mobile toggle
│   ├── Hero.jsx                       # Hero section (homepage)
│   ├── Services.jsx                   # Services grid (homepage)
│   ├── Features.jsx                   # Features section (homepage)
│   ├── Testimonials.jsx               # Testimonials section (homepage)
│   ├── Footer.jsx                     # Footer (all pages)
│   ├── Sidebar.jsx                    # Dashboard sidebar navigation
│   └── DashboardLayout.jsx            # Dashboard layout wrapper

├── data/
│   ├── services.json                  # Homepage services data
│   └── dashboard.json                 # Complete dashboard mock data

├── public/
│   ├── images/
│   │   ├── hero-consultation.jpg      # Hero section image
│   │   ├── doctor-patient.jpg         # Features section image
│   │   ├── virtual-consultation.jpg   # Features section image
│   │   ├── medical-education.jpg      # (optional)
│   │   ├── medical-icons.svg          # Logo (blue background)
│   │   └── medical-icons-white.svg    # Logo (dark background)
│   └── favicon.ico                    # (optional)

├── styles/
│   └── globals.css                    # Global CSS + Tailwind directives

├── Configuration Files
│   ├── tailwind.config.cjs            # Tailwind CSS theme config
│   ├── postcss.config.cjs             # PostCSS configuration
│   ├── next.config.js                 # Next.js configuration
│   ├── package.json                   # Dependencies & scripts
│   └── .gitignore                     # Git ignore rules

└── Documentation Files
    ├── README.md                      # Main quick start guide
    ├── PROJECT_SUMMARY.md             # Project overview
    ├── DASHBOARD_GUIDE.md             # Dashboard pages documentation
    ├── DEPLOYMENT.md                  # Deployment instructions
    ├── FEATURES.md                    # Complete feature inventory
    ├── VISUAL_GUIDE.md                # Visual tour & UX guide
    └── THIS_FILE                      # URLs & file locations
```

## 📊 Data Files Content

### data/services.json
Contains 3 service items for homepage:
- Ask Your Doctor
- Find Jobs
- Medical Courses

**Path**: `d:\phyzioline static html\phyzioline-ui\data\services.json`

### data/dashboard.json
Complete mock data with 4 main sections:

#### Overview Section
- 4 stat items (appointments, courses, messages, balance)
- 3 recent appointments

#### Appointments Section
- 4 full appointments with details

#### Courses Section
- 4 courses with progress levels (75%, 45%, 100%, 0%)

#### Profile Section
- User information (name, email, phone, DOB)
- Address details
- Medical information
- Notification preferences

**Path**: `d:\phyzioline static html\phyzioline-ui\data\dashboard.json`

## 🖼️ Image Files

### Located in: `public/images/`

| Filename | Size | Usage |
|----------|------|-------|
| `hero-consultation.jpg` | ~501KB | Hero section background |
| `doctor-patient.jpg` | ~38KB | Features section |
| `virtual-consultation.jpg` | ~39KB | Features section |
| `medical-education.jpg` | ~130KB | (optional) |
| `medical-icons.svg` | small | Logo (teal background) |
| `medical-icons-white.svg` | small | Logo (dark background) |

**Referenced as**: `/images/filename.ext` in components

## 🛠️ Configuration Details

### tailwind.config.cjs
Defines:
- Primary color (teal #008080)
- Extended colors (primary variants)
- Font family (Inter)
- Shadow definitions
- Border radius

### postcss.config.cjs
Plugins:
- tailwindcss
- autoprefixer

### next.config.js
Settings:
- React strict mode enabled
- Image domains: phyzioline.vercel.app, cdn.jsdelivr.net, etc.

### package.json
Scripts:
- `npm run dev` → Start dev server (port 3000)
- `npm run build` → Production build
- `npm start` → Run production server

## 📚 Documentation Files Summary

| File | Purpose | Read Time |
|------|---------|-----------|
| README.md | Quick start guide | 5 min |
| PROJECT_SUMMARY.md | Project overview & status | 5 min |
| DASHBOARD_GUIDE.md | Dashboard pages & data | 5 min |
| DEPLOYMENT.md | Deploy instructions (3 methods) | 10 min |
| FEATURES.md | Complete feature checklist | 5 min |
| VISUAL_GUIDE.md | Visual tour & UX guide | 10 min |
| THIS_FILE | File locations & URLs | 5 min |

## 🚀 Quick Command Reference

```powershell
# Navigate to project
cd "d:\phyzioline static html\phyzioline-ui"

# Install dependencies
npm install

# Start development server (opens http://localhost:3000)
npm run dev

# Build for production
npm run build

# Run production build
npm start

# Deploy to Vercel
npm i -g vercel
vercel

# View project files
ls -la

# Check Git status
git status

# Add all changes
git add .

# Commit changes
git commit -m "message"

# Push to GitHub
git push origin main
```

## 🔗 Important Links

### Vercel Deployment
- Dashboard: https://vercel.com/dashboard
- After deploy: `https://phyzioline-ui.vercel.app` (example)

### Documentation
- Next.js: https://nextjs.org/docs
- Tailwind: https://tailwindcss.com/docs
- Font Awesome: https://fontawesome.com/icons

### Tools
- Node.js Download: https://nodejs.org
- GitHub: https://github.com/new

## ✅ Files to Update When Integrating Backend

- [x] `/api/dashboard.js` — Connect to real API
- [x] `data/dashboard.json` — Replace with API calls
- [x] `data/services.json` — Replace with API calls
- [x] `pages/dashboard/*.jsx` — Add real data fetching
- [x] `pages/_app.jsx` — Add authentication provider
- [x] Environment variables → Add API endpoint URLs

## 🔐 Environment Variables (Optional)

Create `.env.local` file:
```
NEXT_PUBLIC_API_URL=https://api.phyzioline.com
NEXT_PUBLIC_VERCEL_URL=https://phyzioline-ui.vercel.app
API_SECRET_KEY=your-secret-key
```

Access in code:
```javascript
const apiUrl = process.env.NEXT_PUBLIC_API_URL
```

---

**Last Updated**: Nov 25, 2025  
**Status**: Ready for deployment ✅
