# 🔌 Phyzioline API - دليل الاستخدام

## 📍 Base URL
```
Development: http://localhost:8000/api/v1/
```

---

## 🔐 Authentication Endpoints

### 1. Register (التسجيل)
**POST** `/api/v1/auth/register/`

**Request Body:**
```json
{
  "username": "ahmed123",
  "email": "ahmed@example.com",
  "password": "SecurePass123!",
  "password2": "SecurePass123!",
  "role": "doctor",
  "phone_number": "+201234567890",
  "first_name": "أحمد",
  "last_name": "محمد"
}
```

**Response (201 Created):**
```json
{
  "status": "success",
  "message": "تم التسجيل بنجاح",
  "user": {
    "id": 1,
    "username": "ahmed123",
    "email": "ahmed@example.com",
    "role": "doctor",
    "role_display": "طبيب"
  },
  "tokens": {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}
```

**Available Roles:**
- `patient` - مريض
- `doctor` - طبيب
- `specialist` - أخصائي علاج طبيعي
- `vendor` - مورد أجهزة
- `company` - شركة/مركز طبي
- `trainer` - مدرب/محاضر
- `admin` - مسؤول النظام

---

### 2. Login (تسجيل الدخول)
**POST** `/api/v1/auth/login/`

**Request Body:**
```json
{
  "username": "ahmed123",
  "password": "SecurePass123!"
}
```

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "username": "ahmed123",
    "email": "ahmed@example.com",
    "role": "doctor",
    "role_display": "طبيب"
  },
  "status": "success",
  "message": "تم تسجيل الدخول بنجاح"
}
```

---

### 3. Refresh Token (تجديد الـ Token)
**POST** `/api/v1/auth/refresh/`

**Request Body:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

---

### 4. Logout (تسجيل الخروج)
**POST** `/api/v1/auth/logout/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "تم تسجيل الخروج بنجاح"
}
```

---

## 👤 Profile Endpoints

### 5. Get My Profile (عرض ملف التعريف)
**GET** `/api/v1/accounts/profile/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "ahmed123",
    "email": "ahmed@example.com",
    "first_name": "أحمد",
    "last_name": "محمد",
    "date_joined": "2025-01-27T10:00:00Z"
  },
  "role": "doctor",
  "role_display": "طبيب",
  "phone_number": "+201234567890",
  "bio": "طبيب متخصص في العلاج الطبيعي...",
  "is_verified": false,
  "created_at": "2025-01-27T10:00:00Z"
}
```

---

### 6. Update My Profile (تحديث ملف التعريف)
**PUT** `/api/v1/accounts/profile/` (تحديث كامل)
**PATCH** `/api/v1/accounts/profile/` (تحديث جزئي)

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "user": {
    "first_name": "أحمد",
    "last_name": "محمد",
    "email": "ahmed@example.com"
  },
  "phone_number": "+201234567890",
  "bio": "طبيب متخصص في العلاج الطبيعي مع خبرة 10 سنوات..."
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "ahmed123",
    "email": "ahmed@example.com",
    "first_name": "أحمد",
    "last_name": "محمد",
    "date_joined": "2025-01-27T10:00:00Z"
  },
  "role": "doctor",
  "role_display": "طبيب",
  "phone_number": "+201234567890",
  "bio": "طبيب متخصص في العلاج الطبيعي مع خبرة 10 سنوات...",
  "is_verified": false,
  "created_at": "2025-01-27T10:00:00Z"
}
```

---

### 7. Get Public Profile (عرض ملف تعريف عام)
**GET** `/api/v1/accounts/profile/{id}/`

**No Authentication Required**

**Response (200 OK):**
```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "ahmed123",
    "email": "ahmed@example.com",
    "first_name": "أحمد",
    "last_name": "محمد",
    "date_joined": "2025-01-27T10:00:00Z"
  },
  "role": "doctor",
  "role_display": "طبيب",
  "phone_number": "+201234567890",
  "bio": "طبيب متخصص...",
  "is_verified": false,
  "created_at": "2025-01-27T10:00:00Z"
}
```

---

## 🧪 Testing with cURL

### Register
```bash
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password2": "testpass123",
    "role": "doctor"
  }'
```

### Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

### Get Profile (with token)
```bash
curl -X GET http://localhost:8000/api/v1/accounts/profile/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 🧪 Testing with Postman/Thunder Client

1. **Create Environment:**
   - `base_url`: `http://localhost:8000/api/v1`
   - `access_token`: (set after login)
   - `refresh_token`: (set after login)

2. **Create Requests:**
   - Register → Save tokens to environment
   - Login → Save tokens to environment
   - Get Profile → Use `{{access_token}}` in Authorization header
   - Update Profile → Use `{{access_token}}` in Authorization header

---

## ⚠️ Error Responses

### 400 Bad Request (Validation Error)
```json
{
  "status": "error",
  "errors": {
    "email": ["هذا البريد الإلكتروني مستخدم بالفعل"],
    "password": ["كلمات المرور غير متطابقة"]
  },
  "message": "Validation failed"
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
  "detail": "You do not have permission to perform this action."
}
```

---

## 📝 Notes

- جميع الـ endpoints تتطلب `Content-Type: application/json`
- الـ endpoints المحمية تتطلب `Authorization: Bearer <token>` في الـ header
- Access token صالح لمدة ساعة واحدة
- Refresh token صالح لمدة 7 أيام
- استخدم refresh token لتجديد access token عند انتهاء صلاحيته

---

**Last Updated:** 2025-01-27

