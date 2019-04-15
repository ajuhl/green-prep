from django import forms
from .models import Food, Meal

from django.forms import ModelForm, DateInput


class MealBuilderForm(ModelForm):

    food_1 = forms.ModelChoiceField(initial=Food.objects.get(pk=535),queryset=Food.objects.all().order_by('name'))
    food_1_limit = forms.IntegerField(required=False)
    food_2 = forms.ModelChoiceField(initial=Food.objects.get(pk=1860),queryset=Food.objects.all().order_by('name'))
    food_2_limit = forms.IntegerField(required=False)

    class Meta:
        model = Meal
        fields = ('meal_name','creation_date','protein_goal','carb_goal','fat_goal',)


    def __init__(self, *args, **kwargs):
        super(MealBuilderForm, self).__init__(*args, **kwargs)
