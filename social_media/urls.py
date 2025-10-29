from django.contrib import admin
from django.urls import path, include  # Make sure 'path' is imported
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as auth_views
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Simple API root view
@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Social Media API',
        'endpoints': {
            'admin': '/admin/',
            'auth_register': '/api/auth/register/',
            'auth_login': '/api/auth/login/',
            'posts': '/api/posts/',
            'profiles': '/api/profiles/',
        }
    })

# Simple health check view
def health_check(request):
    from django.http import JsonResponse
    return JsonResponse({"status": "ok", "message": "Server is running"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/auth/', include('accounts.urls')),
    path('api/', include('profiles.urls')),
    path('api/', include('posts.urls')),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api-token-auth'),
    path('health/', health_check, name='health-check'),  # Health check endpoint
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Fallback for testing
urlpatterns += [
    path('', api_root),  # Root URL also points to API root
]