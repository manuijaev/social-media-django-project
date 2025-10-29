from rest_framework import generics, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Post, Comment, Like
from .serializers import PostSerializer, PostCreateSerializer, CommentSerializer
from accounts.models import CustomUser
from accounts.serializers import UserSerializer

class PostListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        return PostSerializer
    
    def get_queryset(self):
        # For news feed - posts from followed users
        if self.request.query_params.get('feed'):
            followed_users = self.request.user.following.all()
            return Post.objects.filter(user__in=followed_users)
        
        # For all posts
        return Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostCreateSerializer
        return PostSerializer

class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)
    
    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(user=self.request.user, post=post)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Post already liked"}, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        like = get_object_or_404(Like, user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked"})

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.method == 'POST':
        like, created = Like.objects.get_or_create(user=request.user, comment=comment)
        if created:
            return Response({"message": "Comment liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Comment already liked"}, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        like = get_object_or_404(Like, user=request.user, comment=comment)
        like.delete()
        return Response({"message": "Comment unliked"})

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'first_name', 'last_name']
    
    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return CustomUser.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        ).exclude(id=self.request.user.id)