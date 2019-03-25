from django.contrib import admin

# Register your models here.
from mealbuilder.models import Food
from mealbuilder.models import Meal
from mealbuilder.models import Day

admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(Day)
