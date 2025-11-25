# Deployment Checklist & Quick Start Guide

## 📋 Pre-Deployment Checklist

Before deploying to Vercel, verify:

- [ ] All components render without errors locally
- [ ] Images are loading from `/public/images/`
- [ ] Dashboard navigation works (all pages accessible)
- [ ] Responsive design works on mobile (check navbar toggle)
- [ ] No console errors in browser DevTools
- [ ] All links are correct (no 404s)

## 🚀 Local Development Setup

### 1. Install Dependencies
```powershell
cd "d:\phyzioline static html\phyzioline-ui"
npm install
```

### 2. Run Development Server
```powershell
npm run dev
```

Server starts on `http://localhost:3000`

### 3. Test the Site
- **Homepage**: `http://localhost:3000/` — hero, services, features, testimonials
- **Dashboard**: `http://localhost:3000/dashboard/overview` — stats and recent activity
- **Appointments**: `http://localhost:3000/dashboard/appointments` — full appointment management
- **Courses**: `http://localhost:3000/dashboard/courses` — course progress and filtering
- **Profile**: `http://localhost:3000/dashboard/profile` — user info and preferences

## 🌐 Deployment Options

### Option 1: Deploy via Vercel CLI (5 minutes)

**Prerequisites**: Node.js 16+ installed

**Steps**:

1. Install Vercel CLI globally (first time only):
```powershell
npm i -g vercel
```

2. From project root, run deploy:
```powershell
cd "d:\phyzioline static html\phyzioline-ui"
vercel
```

3. Follow the interactive prompts:
   - Link to an existing project or create new
   - Select framework: "Next.js"
   - Select root directory: "./"
   - Build settings: Use defaults

4. **Vercel deploys automatically** and provides public URL:
```
✓ Production: https://phyzioline-ui.vercel.app
✓ Preview: https://phyzioline-ui-git-main-yourname.vercel.app
```

### Option 2: Deploy via GitHub + Vercel Dashboard (10 minutes)

**Prerequisites**: GitHub account, Git installed on your machine

**Steps**:

1. Initialize Git repository locally:
```powershell
cd "d:\phyzioline static html\phyzioline-ui"
git init
git add .
git commit -m "Initial commit: Phyzioline dashboard UI"
```

2. Create GitHub repository (visit https://github.com/new):
   - Name: `phyzioline-ui` (or your choice)
   - Description: "Phyzioline medical platform dashboard"
   - Public or Private (your choice)

3. Push code to GitHub:
```powershell
git remote add origin https://github.com/YOUR_USERNAME/phyzioline-ui.git
git branch -M main
git push -u origin main
```

4. Go to https://vercel.com/dashboard
   - Click "Add New" → "Project"
   - Select "Import Git Repository"
   - Find and select `phyzioline-ui`
   - Click "Import"

5. Vercel configuration page appears:
   - Framework: Next.js (auto-detected)
   - Root Directory: `./` (auto-detected)
   - Click "Deploy"

6. **Wait for build to complete** (~2-3 minutes)
   - You'll get a public URL after success

### Option 3: Deploy via Vercel GitHub Integration (Continuous Deployment)

After Option 2 setup, every `git push` to GitHub automatically deploys to Vercel.

```powershell
# After making changes locally:
git add .
git commit -m "Add new features"
git push origin main

# Vercel automatically redeploys within 30 seconds
```

## 📊 Post-Deployment Checklist

After deployment, verify:

- [ ] Public URL is accessible
- [ ] All pages load correctly
- [ ] Images display properly
- [ ] Navigation works (sidebar, navbar)
- [ ] Responsive design works (test on mobile)
- [ ] No console errors
- [ ] Dashboard pages load mock data

## 🔧 Environment Variables (Optional)

If you need to add environment variables (API keys, etc.):

1. Create `.env.local` file in project root:
```
NEXT_PUBLIC_API_URL=https://api.example.com
NEXT_PUBLIC_VERCEL_URL=https://phyzioline-ui.vercel.app
```

2. Access in code:
```javascript
const apiUrl = process.env.NEXT_PUBLIC_API_URL
```

3. In Vercel Dashboard:
   - Go to Project Settings → Environment Variables
   - Add your variables
   - Redeploy

## 📈 Performance Tips

- **Images**: Optimize JPG files (currently ~500KB for hero image)
- **Splitting**: Break dashboard into smaller chunks using dynamic imports
- **Caching**: Vercel handles caching automatically
- **Analytics**: Add Vercel Analytics in `vercel.json`

## 🐛 Troubleshooting

### Build Fails on Vercel
```
Solution: Check build logs in Vercel Dashboard
→ Project Settings → Build & Development
→ View last failed build log
```

### Images Not Showing
```
Solution: Verify paths start with /images/
✓ Correct: /images/hero-consultation.jpg
✗ Wrong: ./images/hero-consultation.jpg
```

### Styles Not Applying
```
Solution: 
1. Clear cache: npm run build
2. Check tailwind.config.cjs content paths
3. Verify styles/globals.css is imported in _app.jsx
```

### Dashboard Not Loading
```
Solution:
1. Check browser console for errors
2. Verify data/dashboard.json exists
3. Check API route is working: /api/dashboard
```

## 📱 Mobile Testing

After deployment, test on different devices:

- **Desktop**: Full layout with sidebar visible
- **Tablet**: Responsive grid adjusts to 2 columns
- **Mobile**: Navbar toggle works, sidebar hidden by default

## 🔒 Security Notes

- **No sensitive data** in mock data (good for demo)
- **Before production**:
  - Remove mock data
  - Add authentication (NextAuth, Firebase, etc.)
  - Use environment variables for API URLs
  - Enable HTTPS (Vercel does this automatically)

## 📞 Support Resources

- **Next.js Docs**: https://nextjs.org/docs
- **Tailwind CSS**: https://tailwindcss.com
- **Vercel Docs**: https://vercel.com/docs
- **GitHub Issues**: Post problems there

## 🎯 Next Phase

After deployment is live:

1. **Connect Backend**: Update API routes to call real endpoints
2. **Add Authentication**: Implement login/register
3. **Database**: Store real user data (MongoDB, PostgreSQL, etc.)
4. **Real-time**: Add WebSockets for notifications
5. **Analytics**: Track user behavior

---

**Your public URL will look like:**
```
https://phyzioline-ui.vercel.app
```

Share this URL with stakeholders for review!
