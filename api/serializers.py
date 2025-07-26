from rest_framework import serializers

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Food, UserLog


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'calories', 'protein', 'carbohydrates', 'fat']

class UserLogSerializer(serializers.ModelSerializer):

    food_id = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), source='food', write_only=True
    )

    food = FoodSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserLog
        fields = ['id', 'user', 'food', 'food_id', 'date', 'quantity']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

