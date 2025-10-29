import requests
import json

# Test user registration
url = "http://127.0.0.1:8000/api/auth/register/"
data = {
    "username": "testuser2",
    "email": "test2@example.com",
    "password": "testpass123",
    "password2": "testpass123"
}

try:
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")