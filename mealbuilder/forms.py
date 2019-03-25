from django import forms
from .models import Food, Meal

class MealBuilderForm(forms.Form):
    meal_name = forms.CharField(label="Meal Name", max_length=25)

