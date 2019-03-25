
from .models import Food, Meal

#gets context from the meal builder form?
class CalculateMeal():
    meal = Meal()
    meal.name = "Dinner"

    meal.save()
    return meal