from django.http import HttpResponse
from django.shortcuts import render

from .forms import MealBuilderForm
from .models import Food, Meal, MealItem
from .simplex import OptimizeMeal

def mealbuilder(request):

    context = {
        'message': 'Hello, world. You\'re at the mealbuilder index.',
    }

    if request.method == 'POST':
        form = MealBuilderForm(request.POST)
        if form.is_valid():
            meal = CreateMealFromFormData(form)
            optimized_meal = OptimizeMeal(meal)
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
    meal = Meal(
        meal_name = form.cleaned_data.get('meal_name'),
        protein_goal = form.cleaned_data.get('protein_goal'),
        carb_goal = form.cleaned_data.get('carb_goal'),
        fat_goal = form.cleaned_data.get('fat_goal')
    )
    meal.save()

    meal_item_1 = meal.mealitem_set.create(
        food = form.cleaned_data.get('food_1'),
        limit = form.cleaned_data.get('food_1_limit')
    )
    meal_item_1.save()


    meal_item_2 = meal.mealitem_set.create(
        food = form.cleaned_data.get('food_2'),
        limit = form.cleaned_data.get('food_2_limit')
    )
    meal_item_2.save()

    return meal
