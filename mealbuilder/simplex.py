
from .models import Food, Meal, MealItem

#gets context from the meal builder form?
def CalculateMeal(meal):

    import ipdb; ipdb.set_trace()

    #how to access just the mealitems with the foreign key to this meal?
    meal_foods = meal.mealitem_set.all()

    calories = 0
    protein = 0
    carbs = 0
    fat = 0

    for item in meal_foods:
        calories += item.food_item.calories
        protein += item.food_item.protein
        carbs += item.food_item.carbs
        fat += item.food_item.fat

    meal.calories = 200
    meal.protein = protein
    meal.carbs = carbs
    meal.fat = fat

    meal.save()
    return meal