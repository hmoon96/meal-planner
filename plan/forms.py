from django import forms
from .models import MealPlan


class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['week', 'monday_food', 'tuesday_food',
                  'wednesday_food', 'thursday_food', 'friday_food',
                  'saturday_food', 'sunday_food']
        widgets = {
            'week': forms.DateInput(attrs={'type': 'date'}),
            'monday_food': forms.Textarea(attrs={'rows': 3}),
            'tuesday_food': forms.Textarea(attrs={'rows': 3}),
            'wednesday_food': forms.Textarea(attrs={'rows': 3}),
            'thursday_food': forms.Textarea(attrs={'rows': 3}),
            'friday_food': forms.Textarea(attrs={'rows': 3}),
            'saturday_food': forms.Textarea(attrs={'rows': 3}),
            'sunday_food': forms.Textarea(attrs={'rows': 3}),
        }
