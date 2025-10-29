import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media.settings')
django.setup()

from django.test import Client

client = Client(HTTP_HOST='127.0.0.1:8000')  # Specify the host

print("Testing endpoints that should work:")
print("=" * 40)

# Test API root
response = client.get('/api/')
print(f"API Root: {response.status_code}")
if response.status_code == 200:
    print("✓ API Root is working!")
    print(f"Response: {response.data}")
else:
    print("✗ API Root failed")

# Test admin login page (should redirect to login)
response = client.get('/admin/')
print(f"Admin: {response.status_code}")
if response.status_code in [200, 302]:
    print("✓ Admin is accessible")
else:
    print("✗ Admin failed")

print("\nTesting complete!")