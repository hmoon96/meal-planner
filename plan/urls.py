from django.urls import path
from . import views


urlpatterns = [
    path('meal_list/', views.MealList.as_view(), name='meal_list'),
    path(
        'meal_detail/<int:pk>/',
        views.MealDetail.as_view(),
        name='meal_detail'
         ),
    path('meal_create/', views.MealCreate.as_view(), name='meal_create'),
    path(
        'meal_update/<int:pk>/',
        views.MealUpdate.as_view(),
        name='meal_update'
         ),
    path(
        'meal_delete/<int:pk>/',
        views.MealDelete.as_view(),
        name='meal_delete'
         ),
]
