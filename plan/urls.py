from django.urls import path
from . import views


urlpatterns = [
    path('', views.MealList, name='index'),
    path('meal_list/', views.MealList, name='meal_list'),
    path('meal/create/', views.CreateMeal, name='meal_create'),
    path('meal/update/<int:id>', views.UpdateMeal, name='meal_update'),
    path('meal/delete/<int:id>', views.DeleteMeal, name='meal_delete'),
]
