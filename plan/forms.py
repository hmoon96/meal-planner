from django import forms
from .models import MealPlan


class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['user', 'week', 'monday_food', 'tuesday_food',
                  'wednesday_food', 'thursday_food', 'friday_food',
                  'saturday_food', 'sunday_food']
