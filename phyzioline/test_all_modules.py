"""
Comprehensive test script for all Phyzioline API modules.
Tests all endpoints to ensure they're working correctly.
"""
import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000/api/v1"

def print_section(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def test_endpoint(method, url, data=None, headers=None, description=""):
    """Test an API endpoint and return the result."""
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, timeout=5)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data, headers=headers, timeout=5)
        elif method.upper() == 'PUT':
            response = requests.put(url, json=data, headers=headers, timeout=5)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers, timeout=5)
        else:
            return False, f"Unknown method: {method}"
        
        status_ok = response.status_code in [200, 201, 204]
        status_text = "[OK]" if status_ok else "[FAIL]"
        print(f"  {status_text} {description or url}")
        print(f"    Status: {response.status_code}")
        
        if response.status_code not in [200, 201, 204] and response.text:
            try:
                error_data = response.json()
                print(f"    Error: {error_data.get('detail', 'Unknown error')}")
            except:
                print(f"    Error: {response.text[:100]}")
        
        return status_ok, response
    except requests.exceptions.ConnectionError:
        print(f"  [FAIL] {description or url}")
        print(f"    Error: Cannot connect to server. Is Django running on port 8000?")
        return False, None
    except Exception as e:
        print(f"  [FAIL] {description or url}")
        print(f"    Error: {str(e)}")
        return False, None

def main():
    print("\n" + "="*60)
    print("  PHYZIOLINE API - COMPREHENSIVE MODULE TEST")
    print("="*60)
    print(f"  Testing at: {BASE_URL}")
    print(f"  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = {}
    
    # 1. Authentication Module
    print_section("1. AUTHENTICATION MODULE")
    auth_token = None
    
    # Register a test user
    register_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "password2": "testpass123",
        "role": "patient"
    }
    success, response = test_endpoint('POST', f"{BASE_URL}/auth/register/", 
                                     data=register_data, 
                                     description="Register new user")
    results['register'] = success
    
    # Try to login with existing user first, if register failed
    login_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    success, response = test_endpoint('POST', f"{BASE_URL}/auth/login/", 
                                     data=login_data, 
                                     description="Login user")
    if success and response:
        try:
            token_data = response.json()
            auth_token = token_data.get('access')
            if auth_token:
                print(f"    [OK] Token obtained: {auth_token[:20]}...")
                headers = {"Authorization": f"Bearer {auth_token}"}
        except:
            pass
    results['login'] = success
    
    # If login failed, try with admin user
    if not auth_token:
        admin_login = {
            "username": "admin",
            "password": "admin123"
        }
        success, response = test_endpoint('POST', f"{BASE_URL}/auth/login/", 
                                         data=admin_login, 
                                         description="Login as admin")
        if success and response:
            try:
                token_data = response.json()
                auth_token = token_data.get('access')
                if auth_token:
                    print(f"    [OK] Admin token obtained: {auth_token[:20]}...")
                    headers = {"Authorization": f"Bearer {auth_token}"}
            except:
                pass
    
    if not auth_token:
        headers = {}
        print("    [WARN] No authentication token available - some tests will fail")
    
    # Get user profile (accounts URLs are included at /api/v1/ so profile is at /api/v1/profile/)
    success, _ = test_endpoint('GET', f"{BASE_URL}/profile/", 
                               headers=headers, 
                               description="Get user profile")
    results['profile'] = success
    
    # 2. Marketplace Module
    print_section("2. MARKETPLACE MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/marketplace/products/", 
                               description="List products")
    results['marketplace_products'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/marketplace/categories/", 
                               description="List categories")
    results['marketplace_categories'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/marketplace/cart/", 
                               headers=headers, 
                               description="Get cart")
    results['marketplace_cart'] = success
    
    # 3. Jobs Module
    print_section("3. JOBS MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/jobs/posts/", 
                               description="List job posts")
    results['jobs_list'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/jobs/applications/", 
                               headers=headers, 
                               description="List job applications")
    results['jobs_applications'] = success
    
    # 4. Courses Module
    print_section("4. COURSES MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/courses/courses/", 
                               description="List courses")
    results['courses_list'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/courses/enrollments/", 
                               headers=headers, 
                               description="List enrollments")
    results['courses_enrollments'] = success
    
    # 5. Clinics Module
    print_section("5. CLINICS MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/clinics/clinics/", 
                               description="List clinics")
    results['clinics_list'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/clinics/appointments/", 
                               headers=headers, 
                               description="List appointments")
    results['clinics_appointments'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/clinics/patients/", 
                               headers=headers, 
                               description="List patients")
    results['clinics_patients'] = success
    
    # 6. Home Sessions Module
    print_section("6. HOME SESSIONS MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/sessions/sessions/", 
                               description="List sessions")
    results['sessions_list'] = success
    
    # 7. Feed Module
    print_section("7. SOCIAL FEED MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/feed/posts/", 
                               description="List posts")
    results['feed_posts'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/feed/comments/", 
                               description="List comments")
    results['feed_comments'] = success
    
    # 8. Ads Module
    print_section("8. ADS MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/ads/campaigns/", 
                               description="List campaigns")
    results['ads_campaigns'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/ads/ads/", 
                               description="List ads")
    results['ads_list'] = success
    
    # 9. AI Engine Module
    print_section("9. AI ENGINE MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/ai/exercises/", 
                               description="List exercises")
    results['ai_exercises'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/ai/treatment-plans/", 
                               headers=headers, 
                               description="List treatment plans")
    results['ai_treatment_plans'] = success
    
    # 10. CRM Module
    print_section("10. CRM MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/crm/campaigns/", 
                               headers=headers, 
                               description="List CRM campaigns")
    results['crm_campaigns'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/crm/contacts/", 
                               headers=headers, 
                               description="List contacts")
    results['crm_contacts'] = success
    
    # 11. Equivalency Module
    print_section("11. EQUIVALENCY MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/equivalency/countries/", 
                               description="List countries")
    results['equivalency_countries'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/equivalency/requirements/", 
                               description="List requirements")
    results['equivalency_requirements'] = success
    
    # 12. Global Stats Module
    print_section("12. GLOBAL STATS MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/global-stats/snapshots/", 
                               description="List snapshots")
    results['global_stats_snapshots'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/global-stats/countries/", 
                               description="List country stats")
    results['global_stats_countries'] = success
    
    # 13. Payments Module
    print_section("13. PAYMENTS MODULE")
    success, _ = test_endpoint('GET', f"{BASE_URL}/payments/gateways/", 
                               headers=headers, 
                               description="List payment gateways")
    results['payments_gateways'] = success
    
    success, _ = test_endpoint('GET', f"{BASE_URL}/payments/transactions/", 
                               headers=headers, 
                               description="List transactions")
    results['payments_transactions'] = success
    
    # Summary
    print_section("TEST SUMMARY")
    total_tests = len(results)
    passed_tests = sum(1 for v in results.values() if v)
    failed_tests = total_tests - passed_tests
    
    print(f"  Total Tests: {total_tests}")
    print(f"  Passed: {passed_tests} [OK]")
    print(f"  Failed: {failed_tests} [FAIL]")
    print(f"  Success Rate: {(passed_tests/total_tests*100):.1f}%")
    
    if failed_tests > 0:
        print("\n  Failed Tests:")
        for test_name, result in results.items():
            if not result:
                print(f"    [FAIL] {test_name}")
    
    print("\n" + "="*60)
    print("  Testing Complete!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

