from django.http import HttpResponse
from django.shortcuts import render

from .forms import MealBuilderForm
from .models import Food, Meal

def mealbuilder(request):

    context = {
        'message': 'Hello, world. You\'re at the mealbuilder index.',
    }

    if request.method == 'POST':
        form = MealBuilderForm(request.POST)
        if form.is_valid():
            meal = CreateMealFromFormData(form)
            #optimized_meal = SimplexMethod(meal)
            context.update({
                'optimized_meal': meal,
                'message': "Form successfully submitted",
            })

    else:
        form = MealBuilderForm()

    context.update({
        'form': form, 
    })
    return render(request, 'mealbuilder.html', context=context)


def CreateMealFromFormData(form):
    print("attempting to create the meal")
    meal = Meal()
    meal.name = form.cleaned_data.get('meal_name')

    meal.save()
    print("meal saved!!" + meal.name + "\n")