from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # Fixed typo: I&uthenticated -> IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Profile  # Fixed import
from .serializers import ProfileSerializer, ProfileUpdateSerializer  # Fixed import
from accounts.models import CustomUser  # Fixed import

class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]  # Fixed typo
    lookup_field = 'user_id'

class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]  # Fixed typo

    def get_object(self):
        return self.request.user.profile

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])  # Fixed typo
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    target_profile = target_user.profile
    
    if request.method == 'POST':
        if request.user != target_user:
            target_profile.followers.add(request.user)
            return Response({"message": f"Now following {target_user.username}"})
        return Response({"error": "Cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if request.user != target_user:
            target_profile.followers.remove(request.user)
            return Response({"message": f"Unfollowed {target_user.username}"})
        return Response({"error": "Cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)