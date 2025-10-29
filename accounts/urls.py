from django.urls import path
from . import views  # Fixed import

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('me/', views.UserDetailView.as_view(), name='user-detail'),
]