# Phyzioline UI - Next.js + Tailwind

A modern **Next.js + Tailwind CSS** healthcare platform with a complete dashboard, responsive design, and teal branding. Built from scratch with mock data and ready for backend integration.

## ✨ Features

✅ **Responsive Design** — Mobile-first Tailwind CSS with navbar toggle  
✅ **Dashboard Pages** — 4 pages (Overview, Appointments, Courses, Profile)  
✅ **Mock Data** — Complete with interactive filtering and state management  
✅ **Teal Branding** — Exact color matching (#008080, #006666, #00a0a0)  
✅ **Local Assets** — SVG logos and images in `public/` folder  
✅ **Production Ready** — Deploy to Vercel in < 5 minutes  

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md) | Overview of the entire project |
| [DASHBOARD_GUIDE.md](./DASHBOARD_GUIDE.md) | Dashboard pages and mock data structure |
| [DEPLOYMENT.md](./DEPLOYMENT.md) | Deployment instructions (3 options) |

**Start here**: Read [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md) first!

## 🚀 Quick Start

### Prerequisites
- **Node.js 16+** (download from https://nodejs.org)

### Run Locally

1. Navigate to project:
```powershell
cd "d:\phyzioline static html\phyzioline-ui"
```

2. Install dependencies:
```powershell
npm install
```

3. Start dev server:
```powershell
npm run dev
```

4. Open in browser:
```
http://localhost:3000
```

### Deploy to Vercel

```powershell
npm i -g vercel
vercel
```

You'll get a public URL like: `https://phyzioline-ui.vercel.app`

## 📁 Project Structure

```
phyzioline-ui/
├── pages/                      # Next.js pages
│   ├── index.jsx              # Homepage
│   ├── api/dashboard.js       # Mock API
│   └── dashboard/             # Dashboard pages
│       ├── overview.jsx
│       ├── appointments.jsx
│       ├── courses.jsx
│       └── profile.jsx
├── components/                # React components
│   ├── Header.jsx            # Navbar (mobile toggle)
│   ├── Sidebar.jsx           # Dashboard sidebar
│   └── ... (Hero, Services, etc.)
├── data/                      # Mock data
│   ├── services.json
│   └── dashboard.json
├── public/images/             # Static assets
├── styles/                    # Global CSS + Tailwind
└── tailwind.config.cjs        # Theme configuration
```

## 🎨 Dashboard Pages

### `/dashboard/overview` — Overview Page
- 4 stat cards (appointments, courses, messages, balance)
- Recent appointments list
- Quick action buttons

### `/dashboard/appointments` — Appointments Management
- Filter: All / Upcoming / Completed
- Full appointment cards with doctor details
- Book, join, and cancel appointments

### `/dashboard/courses` — Course Progress
- Filter: All / In Progress / Completed / Enrolled
- Progress bars and module counters
- Continue learning buttons

### `/dashboard/profile` — User Profile
- Personal information (with avatar)
- Address and medical info
- Notification preferences (toggles)
- Edit mode support

## 🎨 Colors & Theme

All colors match the original design:

```javascript
// In tailwind.config.cjs
colors: {
  primary: {
    light: '#00a0a0',    // teal-light
    DEFAULT: '#008080',  // teal
    dark: '#006666'      // teal-dark
  }
}
```

Use in components: `bg-primary`, `text-primary`, `hover:bg-primary-dark`

## 🔧 Configuration

### Fonts
**Inter** (Google Fonts) — configured in `_app.jsx` and `tailwind.config.cjs`

### Responsive Breakpoints
- **sm**: 640px (mobile)
- **md**: 768px (tablet, navbar toggle appears)
- **lg**: 1024px (desktop)
- **xl**: 1280px (wide desktop)

### Build & Deploy
```powershell
npm run build        # Create production build
npm start           # Start production server
vercel             # Deploy to Vercel
```

## 📊 Mock Data

All mock data is stored in `data/dashboard.json`:

```json
{
  "overview": { stats, recentAppointments },
  "appointments": { appointments array },
  "courses": { courses array },
  "profile": { user, address, medicalInfo, preferences }
}
```

### To Use Real Data

Replace imports:
```javascript
// Before (mock data)
import dashboardData from '../../data/dashboard.json'

// After (real API)
const response = await fetch('/api/appointments')
const dashboardData = await response.json()
```

## 🌐 Deployment Options

### Option 1: Vercel CLI (5 minutes)
```powershell
npm i -g vercel
vercel
```

### Option 2: GitHub + Vercel Dashboard (10 minutes)
1. Push to GitHub
2. Import in Vercel Dashboard
3. Auto-deploy on every push

### Option 3: Traditional Hosting
```powershell
npm run build      # Creates .next/
npm start          # Runs on port 3000
```

👉 See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions

## 🐛 Troubleshooting

**"npm not found"**
→ Install Node.js from https://nodejs.org/

**Port 3000 already in use**
→ Run: `npm run dev -- -p 3001`

**Tailwind styles not showing**
→ Verify `styles/globals.css` is imported in `pages/_app.jsx`

**Images not loading**
→ Check paths start with `/images/` (not `./images/`)

## 🔗 API Routes

### `/api/dashboard`
Returns navigation items and content for dashboard:
```json
{
  "items": [
    {"slug": "overview", "label": "Overview"},
    {"slug": "appointments", "label": "Appointments"},
    {"slug": "courses", "label": "My Courses"},
    {"slug": "profile", "label": "My Profile"}
  ]
}
```

## 📱 Mobile Support

The site is fully responsive:
- **Desktop**: Full sidebar visible
- **Tablet**: Responsive grid (2 columns)
- **Mobile**: Hamburger menu, full-width content

Test on mobile: Press `F12` in browser → Toggle device toolbar

## 🚀 What's Next?

1. ✅ **Test Locally**: `npm install && npm run dev`
2. ✅ **Deploy**: `vercel` command
3. ⬜ **Connect Backend**: Replace mock data with real API
4. ⬜ **Add Auth**: Implement login/register
5. ⬜ **Real Database**: Connect MongoDB/PostgreSQL

## 📞 Support

- **Docs**: [Next.js](https://nextjs.org) · [Tailwind](https://tailwindcss.com) · [Vercel](https://vercel.com/docs)
- **Issues**: Check [DEPLOYMENT.md](./DEPLOYMENT.md) troubleshooting section

---

**Ready to go live? Run `npm install && npm run dev` then `vercel` to deploy! 🚀**

**Version**: 0.2.0 | **Last Updated**: Nov 25, 2025

