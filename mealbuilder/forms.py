from django import forms
from .models import Food, Meal

class MealBuilderForm(forms.Form):
    meal_name = forms.CharField(label="Meal Name", max_length=25)

    food__1 = forms.ModelChoiceField(queryset=Food.objects.all().order_by('name'))
    food_1_quantity = forms.DecimalField(max_digits=6, decimal_places=2)

    food__2 = forms.ModelChoiceField(queryset=Food.objects.all().order_by('name'))
    food_2_quantity = forms.DecimalField(max_digits=6, decimal_places=2)

