from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Post, Food, UserLog
from .serializers import PostSerializer, FoodSerializer, UserLogSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class UserLogViewSet(viewsets.ModelViewSet):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer