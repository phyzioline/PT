# 🔌 Phyzioline API Design
## تصميم واجهات برمجة التطبيقات

---

## 🌐 Base Configuration

### Base URL
```
Development: http://localhost:8000/api/v1/
Production: https://api.phyzioline.com/api/v1/
```

### Authentication
- **Method:** JWT (JSON Web Tokens)
- **Header:** `Authorization: Bearer <token>`
- **Endpoints:**
  - `POST /api/v1/auth/register/` - Register new user
  - `POST /api/v1/auth/login/` - Login (get tokens)
  - `POST /api/v1/auth/refresh/` - Refresh access token
  - `POST /api/v1/auth/logout/` - Logout (blacklist token)

---

## 📱 API Endpoints by App

### 1. **Accounts App** (`/api/v1/accounts/`)

#### Authentication
```
POST   /api/v1/auth/register/
POST   /api/v1/auth/login/
POST   /api/v1/auth/refresh/
POST   /api/v1/auth/logout/
```

**Register Request:**
```json
{
  "username": "ahmed123",
  "email": "ahmed@example.com",
  "password": "SecurePass123!",
  "password2": "SecurePass123!",
  "role": "doctor",
  "phone_number": "+201234567890"
}
```

**Register Response:**
```json
{
  "user": {
    "id": 1,
    "username": "ahmed123",
    "email": "ahmed@example.com",
    "role": "doctor"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}
```

**Login Request:**
```json
{
  "username": "ahmed123",
  "password": "SecurePass123!"
}
```

#### User Profile
```
GET    /api/v1/accounts/profile/          # Get current user profile
PUT    /api/v1/accounts/profile/          # Update current user profile
PATCH  /api/v1/accounts/profile/          # Partial update
GET    /api/v1/accounts/profile/{id}/     # Get specific user profile (public)
```

**Profile Response:**
```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "ahmed123",
    "email": "ahmed@example.com"
  },
  "role": "doctor",
  "phone_number": "+201234567890",
  "bio": "Experienced physiotherapist...",
  "is_verified": true,
  "created_at": "2025-01-27T10:00:00Z"
}
```

---

### 2. **Jobs App** (`/api/v1/jobs/`)

#### Job Posts
```
GET    /api/v1/jobs/                      # List all jobs (with filters)
POST   /api/v1/jobs/                      # Create job (Company only)
GET    /api/v1/jobs/{id}/                 # Get job details
PUT    /api/v1/jobs/{id}/                 # Update job (Owner only)
DELETE /api/v1/jobs/{id}/                 # Delete job (Owner only)
```

**Create Job Request:**
```json
{
  "title": "أخصائي علاج طبيعي مطلوب",
  "description": "نبحث عن أخصائي علاج طبيعي بخبرة 3 سنوات...",
  "location": "القاهرة، مصر",
  "is_full_time": true,
  "salary_range": "8000-12000 EGP"
}
```

**Job Response:**
```json
{
  "id": 1,
  "company": {
    "id": 5,
    "username": "clinic_cairo",
    "role": "company"
  },
  "title": "أخصائي علاج طبيعي مطلوب",
  "description": "...",
  "location": "القاهرة، مصر",
  "is_full_time": true,
  "salary_range": "8000-12000 EGP",
  "posted_at": "2025-01-27T10:00:00Z",
  "applications_count": 3
}
```

**Filters:**
- `?location=القاهرة`
- `?is_full_time=true`
- `?search=أخصائي`
- `?company_id=5`

#### Job Applications
```
GET    /api/v1/jobs/{job_id}/applications/     # List applications (Company owner only)
POST   /api/v1/jobs/{job_id}/apply/             # Apply to job (Specialist only)
GET    /api/v1/jobs/applications/my/            # My applications (Specialist)
GET    /api/v1/jobs/applications/{id}/          # Get application details
PUT    /api/v1/jobs/applications/{id}/status/   # Update status (Company owner only)
```

**Apply Request:**
```json
{
  "cover_letter": "أنا مهتم بهذه الوظيفة لأن..."
}
```

**Application Response:**
```json
{
  "id": 1,
  "job": {
    "id": 1,
    "title": "أخصائي علاج طبيعي مطلوب"
  },
  "applicant": {
    "id": 2,
    "username": "specialist_ahmed",
    "role": "specialist"
  },
  "cover_letter": "...",
  "status": "pending",
  "applied_at": "2025-01-27T11:00:00Z"
}
```

**Update Status Request:**
```json
{
  "status": "interview"
}
```

---

### 3. **Marketplace App** (`/api/v1/marketplace/`) - Phase 2

#### Products
```
GET    /api/v1/marketplace/products/           # List products
POST   /api/v1/marketplace/products/           # Create product (Vendor only)
GET    /api/v1/marketplace/products/{id}/      # Get product details
PUT    /api/v1/marketplace/products/{id}/      # Update product (Owner only)
DELETE /api/v1/marketplace/products/{id}/      # Delete product (Owner only)
```

#### Cart
```
GET    /api/v1/marketplace/cart/               # Get my cart
POST   /api/v1/marketplace/cart/add/           # Add item to cart
PUT    /api/v1/marketplace/cart/update/{id}/   # Update cart item
DELETE /api/v1/marketplace/cart/remove/{id}/   # Remove from cart
```

#### Orders
```
GET    /api/v1/marketplace/orders/             # List my orders
POST   /api/v1/marketplace/orders/checkout/    # Create order from cart
GET    /api/v1/marketplace/orders/{id}/        # Get order details
```

---

## 🔐 Permissions Matrix

| Endpoint | Patient | Doctor | Specialist | Vendor | Company | Trainer | Admin |
|----------|---------|--------|------------|--------|---------|---------|-------|
| Register | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| View Profile | ✅ Own | ✅ Own | ✅ Own | ✅ Own | ✅ Own | ✅ Own | ✅ All |
| Edit Profile | ✅ Own | ✅ Own | ✅ Own | ✅ Own | ✅ Own | ✅ Own | ✅ All |
| Create Job | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Apply to Job | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| View Applications | ❌ | ❌ | ✅ Own | ❌ | ✅ Own Jobs | ❌ | ✅ All |

---

## 📊 Response Format

### Success Response
```json
{
  "status": "success",
  "data": { ... },
  "message": "Operation completed successfully"
}
```

### Error Response
```json
{
  "status": "error",
  "errors": {
    "field_name": ["Error message 1", "Error message 2"]
  },
  "message": "Validation failed"
}
```

### Pagination Response
```json
{
  "count": 100,
  "next": "http://api.example.com/api/v1/jobs/?page=2",
  "previous": null,
  "results": [ ... ]
}
```

---

## 🔍 Filtering & Search

### Common Filters
- `?search=<query>` - Full-text search
- `?ordering=<field>` - Order by field (e.g., `-created_at`)
- `?page=<number>` - Pagination
- `?page_size=<number>` - Items per page

### Job-Specific Filters
- `?location=<location>`
- `?is_full_time=<true|false>`
- `?company_id=<id>`
- `?salary_min=<amount>`
- `?salary_max=<amount>`

---

## 📝 Status Codes

- `200 OK` - Success
- `201 Created` - Resource created
- `204 No Content` - Success (no content)
- `400 Bad Request` - Validation error
- `401 Unauthorized` - Not authenticated
- `403 Forbidden` - Not authorized
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

---

## 🧪 Testing Endpoints

### Using cURL
```bash
# Register
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","email":"test@example.com","password":"pass123","password2":"pass123","role":"doctor"}'

# Login
curl -X POST http://localhost:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"pass123"}'

# Get Profile (with token)
curl -X GET http://localhost:8000/api/v1/accounts/profile/ \
  -H "Authorization: Bearer <access_token>"
```

### Using Postman/Thunder Client
1. Create collection "Phyzioline API"
2. Add environment variables:
   - `base_url`: `http://localhost:8000/api/v1`
   - `access_token`: (set after login)
3. Create requests for each endpoint

---

**Last Updated:** 2025-01-27

