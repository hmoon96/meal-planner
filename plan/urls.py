from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('meal/view/', views.MealView, name='meal_view'),
    path('meal/create/', views.CreateMeal, name='meal_create'),
    path('meal/update/<int:id>', views.UpdateMeal, name='meal_update'),
    path('meal/delete/<int:id>', views.DeleteMeal, name='meal_delete'),
]
