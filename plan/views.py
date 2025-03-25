from django.shortcuts import render, redirect, get_object_or_404
from .models import MealPlan
from .forms import MealPlanForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
# Create a view to display the homepage
# This view will render the home.html template


def Home(request):
    return render(request, 'plan/home.html')


# Create a view to display the meal plans
# This view will render the view.html template
# The view will display all the meal plans created by the user
# The meal plans will be displayed in descending order of the week
# The view will also display a link to create a new meal plan
# The view will also display links to update and delete each meal plan
@login_required
def MealView(request):
    meal_plans = MealPlan.objects.filter(user=request.user).order_by('-week')
    context = {
        "meal_plans": meal_plans,
    }
    return render(request, 'plan/view.html', context)


# Create a view to create a new meal plan
# This view will render the create.html template
# The view will display a form to create a new meal plan
# The form will have fields for the week and the food for each day of the week
# The view will also handle form submission
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
            return render(request, 'plan/create.html', context)
    else:
        form = MealPlanForm()
        context = {
            "form": form,
        }
        return render(request, 'plan/create.html', context)


# Create a view to update a meal plan
# This view will render the update.html template
# The view will display a form to update the meal plan
# The form will have fields for the week and the food for each day of the week
# The view will also handle form submission
# The view will only allow the user who created the meal plan to update it
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
            return render(request, 'plan/update.html', context)
    else:
        form = MealPlanForm(instance=meal_to_update)
        context = {
            "form": form,
        }
        return render(request, 'plan/update.html', context)


# Create a view to delete a meal plan
# This view will render the delete.html template
# The view will display a confirmation message before deleting the meal plan
# The view will also handle form submission
# The view will only allow the user who created the meal plan to delete it
@login_required
def DeleteMeal(request, id):
    meal_to_delete = get_object_or_404(MealPlan, id=id, user=request.user)
    if request.method == 'POST':
        meal_to_delete.delete()
        messages.success(request, 'Meal plan deleted successfully')
        return redirect('meal_view')
    return render(request, 'plan/delete.html')


# Create views for the signup, login, and logout pages
# These views will render signup.html, login.html, and logout.html templates
# The views will also handle form submission
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
