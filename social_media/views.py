from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'admin': reverse('admin:index', request=request, format=format),
        'auth_register': reverse('register', request=request, format=format),
        'auth_login': reverse('login', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
    })