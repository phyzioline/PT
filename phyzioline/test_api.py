import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

print("🧪 اختبار API Endpoints...\n")

# Test 1: Register
print("1. اختبار Register...")
try:
    response = requests.post(
        f"{BASE_URL}/auth/register/",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass123",
            "password2": "testpass123",
            "role": "doctor"
        }
    )
    print(f"   Status: {response.status_code}")
    if response.status_code == 201:
        print("   ✅ Register يعمل!")
        data = response.json()
        print(f"   User ID: {data.get('user', {}).get('id')}")
    else:
        print(f"   ❌ Error: {response.text}")
except Exception as e:
    print(f"   ❌ Connection Error: {e}")

print("\n2. اختبار Login...")
try:
    response = requests.post(
        f"{BASE_URL}/auth/login/",
        json={
            "username": "admin",
            "password": "admin123"
        }
    )
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        print("   ✅ Login يعمل!")
        data = response.json()
        print(f"   Access Token: {data.get('access', '')[:50]}...")
    else:
        print(f"   ❌ Error: {response.text}")
except Exception as e:
    print(f"   ❌ Connection Error: {e}")

print("\n3. اختبار Products List...")
try:
    response = requests.get(f"{BASE_URL}/marketplace/products/")
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        print("   ✅ Products API يعمل!")
    else:
        print(f"   ❌ Error: {response.text}")
except Exception as e:
    print(f"   ❌ Connection Error: {e}")

print("\n✅ انتهى الاختبار!")

