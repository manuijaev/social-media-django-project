from django.urls import path
from . import views

urlpatterns = [
    path('profiles/<int:user_id>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profiles/me/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('users/<int:user_id>/follow/', views.follow_user, name='follow-user'),
]