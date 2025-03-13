from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, TemplateView
from .models import MealPlan
from .forms import MealPlanForm


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


class IndexView(TemplateView):
    template_name = 'plan/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MealPlanForm()
        return context

    def post(self, request, *args, **kwargs):
        form = MealPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
        return self.render_to_response(self.get_context_data(form=form))
