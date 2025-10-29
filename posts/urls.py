from django.urls import path
from . import views

urlpatterns = [
    # Post endpoints
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    
    # Comment endpoints
    path('posts/<int:post_id>/comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    
    # Like endpoints
    path('posts/<int:post_id>/like/', views.like_post, name='like-post'),
    path('comments/<int:comment_id>/like/', views.like_comment, name='like-comment'),
    
    # Search endpoints
    path('search/users/', views.UserSearchView.as_view(), name='user-search'),
]