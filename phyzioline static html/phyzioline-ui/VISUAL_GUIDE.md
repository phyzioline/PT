# Visual Tour & User Experience

## 🎨 Color Scheme

### Primary Colors
```
Teal (#008080) - Main brand color
├── Light Teal (#00a0a0) - Hover states
├── Dark Teal (#006666) - Pressed states
└── Teal with opacity - Backgrounds
```

### Status/Semantic Colors
```
Success Green (#28a745) - Completed, approved
Info Blue (#17a2b8) - Information, in progress
Warning Yellow (#ffc107) - Alerts, pending
Danger Red (#dc3545) - Errors, destructive
```

### Neutral Colors
```
Dark Gray (#343a40) - Text
Light Gray (#f8f9fa) - Backgrounds
White (#ffffff) - Cards, buttons
```

## 📱 Responsive Behavior

### Mobile (< 640px)
```
Header: 
  ├── Logo + brand name
  ├── Hamburger menu button
  └── Login button

Content: Full width, stacked layout

Dashboard: 
  ├── Header (sticky)
  ├── Sidebar hidden (drawer/modal when needed)
  └── Full-width content
```

### Tablet (640px - 1024px)
```
Header: Full navigation visible, buttons visible

Dashboard:
  ├── 2-column grids
  ├── Sidebar visible but narrow
  └── Adjusted spacing

Content: 2 columns for cards/tables
```

### Desktop (> 1024px)
```
Header: Full horizontal navigation

Dashboard:
  ├── Sidebar always visible (240px)
  ├── Main content area
  └── 3-column grids for cards

Content: Full optimization
```

## 🖥️ Page Layouts

### Homepage
```
┌─────────────────────────────────────┐
│ Header (Logo, Nav, Login)           │
├─────────────────────────────────────┤
│ Hero Section (Large heading, CTA)   │
├─────────────────────────────────────┤
│ Services (3 Cards Grid)             │
├─────────────────────────────────────┤
│ Features (Text + 2 Images)          │
├─────────────────────────────────────┤
│ Testimonials (3 Cards)              │
├─────────────────────────────────────┤
│ CTA Section (Call to Action)        │
├─────────────────────────────────────┤
│ Footer (Dark teal, links)           │
└─────────────────────────────────────┘
```

### Dashboard Layout
```
┌─────────────────────────────────────┐
│ Header (Fixed, sticky top-16)       │
├──────────┬──────────────────────────┤
│          │ Page Content             │
│ Sidebar  │ (full width, scrollable) │
│ (fixed)  │                          │
│          │                          │
└──────────┴──────────────────────────┘
```

## 📊 Dashboard Pages - Visual Structure

### Overview Page
```
┌─────────────────────────────────────┐
│ Welcome Back!                       │
├─────────────────────────────────────┤
│ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │
│ │ 12  │ │  3  │ │  8  │ │$250 │  │
│ │Apps │ │Cor  │ │Msg  │ │Bal  │  │
│ └─────┘ └─────┘ └─────┘ └─────┘  │
├─────────────────────────────────────┤
│ Recent Appointments                 │
│ ┌─────────────────────────────────┐ │
│ │ Dr. Sarah | Cardio | Nov 28     │ │
│ │ Dr. Michael | GP | Nov 25       │ │
│ │ Dr. Emily | Peds | Nov 20       │ │
│ └─────────────────────────────────┘ │
├─────────────────────────────────────┤
│ Quick Actions (3 Buttons)           │
└─────────────────────────────────────┘
```

### Appointments Page
```
┌──────────────────────────────────────┐
│ My Appointments    [Book New]        │
├──────────────────────────────────────┤
│ [All] [Upcoming] [Completed]        │
├──────────────────────────────────────┤
│ ┌─────────────────┐ ┌─────────────┐ │
│ │ Dr. Name        │ │ Dr. Name    │ │
│ │ Specialty       │ │ Specialty   │ │
│ │ Date & Time     │ │ Date & Time │ │
│ │ [Join] [Cancel] │ │ [Join]      │ │
│ └─────────────────┘ └─────────────┘ │
│ ┌─────────────────┐ ┌─────────────┐ │
│ │ ...             │ │ ...         │ │
│ └─────────────────┘ └─────────────┘ │
└──────────────────────────────────────┘
```

### Courses Page
```
┌────────────────────────────────────────┐
│ My Courses               [Browse]      │
├────────────────────────────────────────┤
│ [4 Total] [3 Progress] [1 Done] [0]  │
│ [All] [In Progress] [Completed] [E]  │
├────────────────────────────────────────┤
│ ┌──────────┐ ┌──────────┐ ┌─────────┐ │
│ │  [📕]    │ │  [📕]    │ │ [📕]    │ │
│ │ Course   │ │ Course   │ │ Course  │ │
│ │ by Dr.   │ │ by Dr.   │ │ by Dr.  │ │
│ │ ▓▓▓▓░    │ │ ▓▓░░░    │ │ ▓▓▓▓▓   │ │
│ │ 75%      │ │ 45%      │ │ 100%    │ │
│ │ 6/8 Mod  │ │ 5/12 Mod │ │ 10/10   │ │
│ │[Cont][S] │ │[Cont][S] │ │[Cont][S]│ │
│ └──────────┘ └──────────┘ └─────────┘ │
└────────────────────────────────────────┘
```

### Profile Page
```
┌─────────────────────────────────────┐
│ My Profile               [Edit]      │
├─────────────────────────────────────┤
│ [👤] John Smith                     │
│ ──────────────────────────────────   │
│ Personal Information                │
│ ├─ Full Name: John Smith            │
│ ├─ Email: john@example.com          │
│ ├─ Phone: +1 (555) 123-4567         │
│ └─ DOB: 1990-05-15                  │
├─────────────────────────────────────┤
│ Address Information                 │
│ ├─ Street: 123 Medical St           │
│ ├─ City: New York                   │
│ └─ Country: United States           │
├─────────────────────────────────────┤
│ Medical Information                 │
│ ├─ Blood Type: O+                   │
│ ├─ Allergies: Penicillin, Nuts      │
│ └─ Conditions: Hypertension         │
├─────────────────────────────────────┤
│ Notifications                       │
│ ├─ Email: [Toggle ON]               │
│ ├─ SMS: [Toggle OFF]                │
│ ├─ Appointments: [Toggle ON]        │
│ └─ Courses: [Toggle ON]             │
├─────────────────────────────────────┤
│ [⚠️ DANGER] Change Password / Delete │
└─────────────────────────────────────┘
```

## 🎬 User Interactions

### Navbar Toggle (Mobile)
```
User clicks hamburger icon
    ↓
Menu slides down (or appears as overlay)
    ↓
User clicks link (or hamburger again)
    ↓
Menu slides up (or disappears)
```

### Filter Tabs (Appointments/Courses)
```
User clicks filter tab (e.g., "Upcoming")
    ↓
Page filters data
    ↓
Only "Upcoming" items show
    ↓
Tab underline changes to teal
```

### Cancel Appointment
```
User clicks [Cancel] button
    ↓
Appointment card disappears (state update)
    ↓
If all appointments cancelled, empty state shows
```

### Edit Profile
```
User clicks [Edit] button
    ↓
Button changes to [Cancel]
    ↓
Edit icons appear next to each field
    ↓
User makes changes
    ↓
User clicks [Save Changes] or [Cancel]
```

### Toggle Preferences
```
User clicks toggle switch
    ↓
Switch animates left/right
    ↓
Background color changes
    ↓
Preference is saved to state
```

## 🎨 Typography

### Headings
```
h1: 3xl / 32px (hero section)
h2: 2xl / 24px (page titles)
h3: lg / 18px (section titles)
h4/h5: base / 16px (card titles)
```

### Body Text
```
Lead: 1.25rem / 20px (hero subtitle)
Body: base / 16px (normal text)
Small: sm / 14px (metadata)
Xs: xs / 12px (badges)
```

### Font Weights
```
Regular: 400 (body text)
Medium: 500 (labels)
Semibold: 600 (card titles)
Bold: 700 (headings)
```

## ⏱️ Animations

### Hover Effects
```
Cards: Lift up 10px, shadow increases
Buttons: Scale slightly, shadow increases
Links: Color changes, underline appears
Icons: Scale 1.1 on parent hover
```

### Transitions
```
Duration: 300ms (all 0.3s ease)
Property: all (background, transform, shadow)
Easing: cubic-bezier(0.4, 0, 0.2, 1)
```

### Progress Bars
```
Animation: Width changes over 500ms
Direction: Left to right
Duration: 0.5s (transition-all duration-500)
```

## 🎯 Accessibility

- Semantic HTML (header, nav, main, aside, footer)
- Color contrast meets WCAG AA standards
- Icon labels and text alternatives
- Keyboard navigation support
- Focus states on buttons
- Skip to main content (optional)

---

This visual guide helps understand the layout, interactions, and styling of the complete Phyzioline dashboard.
