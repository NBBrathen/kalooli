from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from rest_framework import viewsets, generics, permissions, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Food, UserLog, UserProfile
from .serializers import PostSerializer, FoodSerializer, UserLogSerializer, RegisterSerializer, UserProfileSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'brand',]

class UserLogViewSet(viewsets.ModelViewSet):
    serializer_class = UserLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserLog.objects.filter(user=user)

class RegisterView(generics.CreateAPIView):
    queryset = UserLog.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)