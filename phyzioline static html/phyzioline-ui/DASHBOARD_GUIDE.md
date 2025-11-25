# Dashboard Pages - Complete

This document describes the dashboard pages and mock data structure.

## Pages Included

### 1. **Overview** (`/dashboard/overview`)
Shows key metrics and recent activity:
- **Stats Cards**: Total Appointments, Active Courses, Messages, Account Balance
- **Recent Appointments**: List of upcoming and completed appointments
- **Quick Actions**: Buttons to book appointments, view courses, access medical records

### 2. **Appointments** (`/dashboard/appointments`)
Full appointment management:
- **Book Button**: Create new appointment
- **Filter Tabs**: All, Upcoming, Completed
- **Appointment Cards**: Full details with join video call and cancel options
- **State Management**: Cancel appointments to remove from list

### 3. **Courses** (`/dashboard/courses`)
Learning management:
- **Browse Button**: To explore new courses
- **Stats**: Total, In Progress, Completed, Not Started counts
- **Filter Tabs**: All Courses, In Progress, Completed, Enrolled
- **Course Cards**: Progress bars, module count, Continue/Save buttons
- **Status Badges**: Completed, In Progress, Enrolled

### 4. **Profile** (`/dashboard/profile`)
Account management:
- **Edit Mode**: Toggle to enable/disable editing
- **Sections**:
  - Personal Information (name, email, phone, DOB, gender, avatar)
  - Address Information (street, city, state, zip, country)
  - Medical Information (blood type, allergies, conditions, medications)
  - Notification Preferences (toggles for notifications)
  - Danger Zone (change password, delete account)
- **Interactive Toggles**: For notification preferences

## Mock Data Structure

All mock data is stored in `data/dashboard.json`:

```json
{
  "overview": { stats, recentAppointments },
  "appointments": { appointments array },
  "courses": { courses array },
  "profile": { user, address, medicalInfo, preferences }
}
```

### Data Loading

**API Route** (`/api/dashboard.js`):
- Returns navigation items
- Can be extended to return dynamic content

**Direct Import** (Current):
- Pages import `data/dashboard.json` directly
- Easy to replace with API calls later

## Component Hierarchy

```
DashboardLayout (with Header & Sidebar)
├── Header (top navigation)
├── Sidebar (dynamic nav with icons)
└── Page Content
    ├── Overview Page
    ├── Appointments Page
    ├── Courses Page
    └── Profile Page
```

## Features Implemented

✅ **Dynamic Navigation**: Sidebar highlights current page  
✅ **Responsive Sidebar**: On desktop, sticky at top-16  
✅ **Filter Tabs**: Interactive filtering with state management  
✅ **Progress Bars**: Animated course progress visualization  
✅ **Interactive Toggles**: Preference toggles with visual feedback  
✅ **State Management**: Cancel appointments, filter courses  
✅ **Accessibility**: Icons, proper contrast, semantic HTML  
✅ **Teal Branding**: All buttons and accents use primary color  

## Customization

### Changing Mock Data
Edit `data/dashboard.json` and changes reflect immediately.

### Adding New Dashboard Pages
1. Create file: `pages/dashboard/newpage.jsx`
2. Import DashboardLayout
3. Add navigation item to Sidebar defaultItems
4. Build your content

### Connecting to Real API
Replace in each page:
```javascript
import dashboardData from '../../data/dashboard.json'
```

With:
```javascript
// Fetch from API instead
const response = await fetch('/api/your-endpoint')
const dashboardData = await response.json()
```

## Styling Notes

- **Colors**: Primary teal (#008080), success green (#28a745), info blue (#17a2b8), warning yellow (#ffc107)
- **Shadows**: `shadow-sm`, `shadow-md`, `shadow-lg` on hover
- **Spacing**: Consistent 4px grid (Tailwind defaults)
- **Responsive**: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` patterns

## Next Steps

1. **Connect Backend**: Replace mock data with API endpoints
2. **Add Authentication**: Verify user before showing dashboard
3. **Expand Pages**: Add more dashboard sections as needed
4. **Upload Media**: Replace avatars and course images
5. **Real-time Updates**: Use WebSockets for live notifications
