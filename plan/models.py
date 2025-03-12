from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MealPlan(models.Model):
    user = models.ForeignKey(
        'auth.User',
        related_name='meal_plans',
        on_delete=models.CASCADE
    )
    week = models.DateField()
    monday_food = models.TextField()
    tuesday_food = models.TextField()
    wednesday_food = models.TextField()
    thursday_food = models.TextField()
    friday_food = models.TextField()
    saturday_food = models.TextField()
    sunday_food = models.TextField()
