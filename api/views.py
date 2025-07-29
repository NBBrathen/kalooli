from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated

from .models import Post, Food, UserLog
from .serializers import PostSerializer, FoodSerializer, UserLogSerializer, RegisterSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class UserLogViewSet(viewsets.ModelViewSet):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer
    permission_classes = [IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    queryset = UserLog.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer