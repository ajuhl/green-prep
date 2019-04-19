from django import forms
from .models import Food, Meal

class MealBuilderForm(forms.Form):
    meal_name = forms.CharField(label="Meal Name", max_length=25)
    protein_goal = forms.IntegerField(initial=50) #this will be initialized from day goalMacros
    carb_goal = forms.IntegerField(initial=30)
    fat_goal = forms.IntegerField(initial=20)
#param for ModelChoiceField -> initial=Food.objects.get(pk=535),
    food_1 = forms.ModelChoiceField(queryset=Food.objects.all().order_by('name'))
    food_1_limit = forms.IntegerField(required=False)

#param for ModelChoiceField -> initial=Food.objects.get(pk=1860),
    food_2 = forms.ModelChoiceField(queryset=Food.objects.all().order_by('name'))
    food_2_limit = forms.IntegerField(required=False)
