from rest_framework import serializers

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Post, Food, UserLog, UserProfile



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


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Passwords must match.')
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['daily_calorie_goal', 'daily_protein_goal', 'daily_carb_goal', 'daily_fat_goal']