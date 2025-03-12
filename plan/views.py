from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import MealPlan


class MealList(ListView):
    model = MealPlan
    template_name = 'plan/index.html'
    context_object_name = 'meal_plans'


class MealDetail(UpdateView):
    model = MealPlan
    template_name = 'plan/detail.html'
    fields = '__all__'
    context_object_name = 'meal_plan'


class MealCreate(UpdateView):
    model = MealPlan
    template_name = 'plan/create.html'
    fields = '__all__'
    context_object_name = 'meal_plan'


class MealUpdate(UpdateView):
    model = MealPlan
    template_name = 'plan/update.html'
    fields = '__all__'
    context_object_name = 'meal_plan'


class MealDelete(UpdateView):
    model = MealPlan
    template_name = 'plan/delete.html'
    fields = '__all__'
    context_object_name = 'meal_plan'