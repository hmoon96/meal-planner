from django.urls import path
from .views import IndexView, MealList, MealDetail, MealCreate, MealUpdate
from .views import MealDelete

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('meal_list/', MealList.as_view(), name='meal_list'),
    path('meal/<int:pk>/', MealDetail.as_view(), name='meal_detail'),
    path('meal/create/', MealCreate.as_view(), name='meal_create'),
    path('meal/update/<int:pk>/', MealUpdate.as_view(), name='meal_update'),
    path('meal/delete/<int:pk>/', MealDelete.as_view(), name='meal_delete'),
]
