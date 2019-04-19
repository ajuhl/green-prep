from django import forms
from .models import Food, Meal

from django.forms import ModelForm, DateInput


class MealBuilderForm(ModelForm):

    protein_goal = forms.IntegerField(initial=50) #this will be initialized from day goalMacros
    carb_goal = forms.IntegerField(initial=30)
    fat_goal = forms.IntegerField(initial=20)
    food_1 = forms.ModelChoiceField(queryset=Food.objects.all().order_by('name'))
    food_1_limit = forms.IntegerField(required=False)
    food_2 = forms.ModelChoiceField(queryset=Food.objects.all().order_by('name'))
    food_2_limit = forms.IntegerField(required=False)

    class Meta:
        model = Meal
        fields = ('meal_name',)


    def __init__(self, *args, **kwargs):
        super(MealBuilderForm, self).__init__(*args, **kwargs)
