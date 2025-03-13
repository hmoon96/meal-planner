from django.urls import path
from .views import IndexView, MealList, MealCreate, MealUpdate, MealDelete


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('meal_list/', MealList.as_view(), name='meal_list'),
    path('meal/create/', MealCreate.as_view(), name='meal_create'),
    path('meal/update/', MealUpdate.as_view(), name='meal_update'),
    path('meal/delete/', MealDelete.as_view(), name='meal_delete'),
]
