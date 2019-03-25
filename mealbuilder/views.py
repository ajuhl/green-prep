from django.http import HttpResponse
from django.shortcuts import render

from .forms import MealBuilderForm
from .models import Food, Meal, MealItem
from .simplex import CalculateMeal

def mealbuilder(request):

    context = {
        'message': 'Hello, world. You\'re at the mealbuilder index.',
    }

    if request.method == 'POST':
        form = MealBuilderForm(request.POST)
        if form.is_valid():
            meal = CreateMealFromFormData(form)
            optimized_meal = CalculateMeal(meal)
            context.update({
                'optimized_meal': meal,
                'message': meal.meal_name + " successfully created",
            })

    else:
        form = MealBuilderForm()

    context.update({
        'form': form, 
    })
    return render(request, 'mealbuilder.html', context=context)


def CreateMealFromFormData(form):
    meal = Meal()
    #meal.creator_id = request.user ?
    meal.meal_name = form.cleaned_data.get('meal_name')

    meal_item_1 = MealItem() 
    meal_item_1.meal = meal
    meal_item_1.food_item = form.cleaned_data.get('food_1')
    meal_item_1.food_proportion = form.cleaned_data.get('food_1_quantity')

    meal_item_2 = MealItem() 
    meal_item_2.meal = meal
    meal_item_2.food_item = form.cleaned_data.get('food_2')
    meal_item_2.food_proportion = form.cleaned_data.get('food_2_quantity')

    meal.save()
    return meal