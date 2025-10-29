import requests

print("Testing API endpoints with running server:")
print("=" * 50)

base_url = "http://127.0.0.1:8000"

endpoints = [
    '/',
    '/api/',
    '/admin/',
    '/api/auth/register/',
    '/health/'
]

for endpoint in endpoints:
    try:
        response = requests.get(f"{base_url}{endpoint}")
        print(f"{endpoint}: Status {response.status_code}")
        if response.status_code == 200:
            print("  ✓ Working!")
        elif response.status_code == 404:
            print("  ✗ Not found")
        elif response.status_code == 403:
            print("  ⚠ Requires authentication")
    except requests.exceptions.ConnectionError:
        print(f"{endpoint}: ✗ Connection failed - make sure server is running")
    except Exception as e:
        print(f"{endpoint}: ✗ Error - {e}")