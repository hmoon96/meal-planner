from django.shortcuts import render
from django.views.generic import ListView
from .models import MealPlan


def meal_list(request):
    meal_plans = MealPlan.objects.all()
    return render(request, 'plan/index.html', {'meal_plans': meal_plans})



class MealList(ListView):
    model = MealPlan
    template_name = 'plan/index.html'
    context_object_name = 'meal_plans'