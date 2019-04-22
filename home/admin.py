from django.contrib import admin

from .models import Day, Food, Meal, MealItem

# Register your models here.
admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(MealItem)
admin.site.register(Day)
