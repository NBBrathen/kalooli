from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.FloatField()
    protein = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    fat = models.FloatField(default=0)

    def __str__(self):
        return self.name

class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.FloatField(default=1.0)

    def __str__(self):
        return f'{self.user.username} - {self.food.name} on {self.date}'



