# Phyzioline API - Quick Links Reference

**Base URL:** `http://localhost:8000`

---

## 🔗 Quick Links

### Main Entry Points
- **API Root:** http://localhost:8000/api/v1/
- **Admin Panel:** http://localhost:8000/admin/
- **Frontend:** http://localhost:3000/

---

## 📋 Module Quick Links

### 1. Authentication
- Register: http://localhost:8000/api/v1/auth/register/
- Login: http://localhost:8000/api/v1/auth/login/
- Profile: http://localhost:8000/api/v1/profile/

### 2. Marketplace
- Products: http://localhost:8000/api/v1/marketplace/products/
- Categories: http://localhost:8000/api/v1/marketplace/categories/
- Cart: http://localhost:8000/api/v1/marketplace/cart/
- Orders: http://localhost:8000/api/v1/marketplace/orders/

### 3. Jobs
- Job Posts: http://localhost:8000/api/v1/jobs/posts/
- Applications: http://localhost:8000/api/v1/jobs/applications/

### 4. Courses
- Courses: http://localhost:8000/api/v1/courses/courses/
- Enrollments: http://localhost:8000/api/v1/courses/enrollments/
- Certificates: http://localhost:8000/api/v1/courses/certificates/

### 5. Clinics
- Clinics: http://localhost:8000/api/v1/clinics/clinics/
- Appointments: http://localhost:8000/api/v1/clinics/appointments/
- Patients: http://localhost:8000/api/v1/clinics/patients/
- Invoices: http://localhost:8000/api/v1/clinics/invoices/

### 6. Home Sessions
- Sessions: http://localhost:8000/api/v1/sessions/sessions/
- Availability: http://localhost:8000/api/v1/sessions/availability/

### 7. Social Feed
- Posts: http://localhost:8000/api/v1/feed/posts/
- Comments: http://localhost:8000/api/v1/feed/comments/

### 8. Ads
- Campaigns: http://localhost:8000/api/v1/ads/campaigns/
- Ads: http://localhost:8000/api/v1/ads/ads/

### 9. AI Engine
- Exercises: http://localhost:8000/api/v1/ai/exercises/
- Treatment Plans: http://localhost:8000/api/v1/ai/treatment-plans/

### 10. CRM
- Campaigns: http://localhost:8000/api/v1/crm/campaigns/
- Contacts: http://localhost:8000/api/v1/crm/contacts/
- Messages: http://localhost:8000/api/v1/crm/messages/

### 11. Equivalency
- Countries: http://localhost:8000/api/v1/equivalency/countries/
- Requirements: http://localhost:8000/api/v1/equivalency/requirements/

### 12. Global Stats
- Snapshots: http://localhost:8000/api/v1/global-stats/snapshots/
- Country Stats: http://localhost:8000/api/v1/global-stats/countries/

### 13. Payments
- Gateways: http://localhost:8000/api/v1/payments/gateways/
- Transactions: http://localhost:8000/api/v1/payments/transactions/

---

## 🔑 Authentication

للاستخدام مع Postman أو أي API client:

1. **تسجيل الدخول:**
   ```
   POST http://localhost:8000/api/v1/auth/login/
   Body: {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. **استخدام Token:**
   ```
   Header: Authorization: Bearer <access_token>
   ```

---

## 📱 Frontend Links

- **Homepage:** http://localhost:3000/
- **Dashboard:** http://localhost:3000/dashboard
- **Marketplace:** http://localhost:3000/marketplace
- **Jobs:** http://localhost:3000/jobs
- **Courses:** http://localhost:3000/courses

---

**Tip:** افتح `API_ENDPOINTS.md` للحصول على تفاصيل كاملة عن جميع الـ endpoints.



