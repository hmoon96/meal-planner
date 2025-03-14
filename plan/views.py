from django.shortcuts import render, redirect, get_object_or_404
from .models import MealPlan
from .forms import MealPlanForm


def Home(request):
    return render(request, 'plan/home.html')


def MealView(request):
    meal_plans = MealPlan.objects.all()
    context = {
        "meal_plans": meal_plans,
    }
    return render(request, 'plan/view.html', context)


def CreateMeal(request):
    if request.method == "POST":
        plan = MealPlanForm(request.POST)
        if plan.is_valid():
            plan.save()
            return redirect("meal_view")
        else:
            context = {
                "form": plan,
                "errors": plan.errors,  # Pass form errors to the context
            }
            return render(request, 'plan/create.html', context)
    else:
        form = MealPlanForm()
        context = {
            "form": form,
        }
        return render(request, 'plan/create.html', context)


def UpdateMeal(request, id):
    meal_to_update = get_object_or_404(MealPlan, id=id)
    if request.method == "POST":
        plan = MealPlanForm(request.POST, instance=meal_to_update)
        plan.save()
        return redirect("meal_view")
    else:
        form = MealPlanForm(instance=meal_to_update)
        context = {
            "form": form,
        }
        return render(request, 'plan/update.html', context)


def DeleteMeal(request, id):
    meal_to_delete = get_object_or_404(MealPlan, id=id)
    if request.method == 'POST':
        meal_to_delete.delete()
        return redirect('meal_view')
    return render(request, 'plan/delete.html')
