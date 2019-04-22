from django.contrib import admin

from .models import Plan, Food, Meal, MealFood, SavedMeal, SavedPlan, Event

# Register your models here.
admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(MealFood)
admin.site.register(Plan)
admin.site.register(SavedMeal)
admin.site.register(SavedPlan)
admin.site.register(Event)
