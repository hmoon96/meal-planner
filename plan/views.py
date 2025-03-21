from django.shortcuts import render, redirect, get_object_or_404
from .models import MealPlan
from .forms import MealPlanForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def Home(request):
    return render(request, 'plan/home.html')


@login_required
def MealView(request):
    meal_plans = MealPlan.objects.filter(user=request.user).order_by('-week')
    context = {
        "meal_plans": meal_plans,
    }
    return render(request, 'plan/view.html', context)


@login_required
def CreateMeal(request):
    if request.method == "POST":
        plan = MealPlanForm(request.POST)
        if plan.is_valid():
            meal_plan = plan.save(commit=False)
            meal_plan.user = request.user
            plan.save()
            messages.success(request, 'Meal plan created successfully')
            return redirect("meal_view")
        else:
            context = {
                "form": plan,
                "errors": plan.errors,  # Pass form errors to the context
            }
            messages.error(request, 'Your Meal Plan has not been created')
            return render(request, 'plan/create.html', context)
    else:
        form = MealPlanForm()
        context = {
            "form": form,
        }
        return render(request, 'plan/create.html', context)


@login_required
def UpdateMeal(request, id):
    meal_to_update = get_object_or_404(MealPlan, id=id, user=request.user)
    if request.method == "POST":
        plan = MealPlanForm(request.POST, instance=meal_to_update)
        if plan.is_valid():
            plan.save()
            messages.success(request, 'Meal plan updated successfully')
            return redirect("meal_view")
        else:
            context = {
                "form": plan,
                "errors": plan.errors,  # Pass form errors
            }
            message.error(request, 'There were errors in your form, please make sure every box is filled in.')
            return render(request, 'plan/update.html', context)
    else:
        form = MealPlanForm(instance=meal_to_update)
        context = {
            "form": form,
        }
        return render(request, 'plan/update.html', context)


@login_required
def DeleteMeal(request, id):
    meal_to_delete = get_object_or_404(MealPlan, id=id, user=request.user)
    if request.method == 'POST':
        meal_to_delete.delete()
        messages.success(request, 'Meal plan deleted successfully')
        return redirect('meal_view')
    return render(request, 'plan/delete.html')


def SignUp(request):
    if request.method == 'POST':
        messages.success(request, 'You signed up successfully')
        return redirect('home')
    return render(request, 'plan/signup.html')


def Login(request):
    if request.method == 'POST':
        messages.success(request, 'You are now logged in')
        return redirect('home')
    else:
        messages.error(request, 'Invalid username or password')
    return render(request, 'plan/login.html')


def Logout(request):
    return render(request, 'plan/logout.html')
