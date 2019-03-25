from django.db import models
from django.utils import timezone
from uuid import uuid4
import datetime

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=120)
    #serving_sizes(S)  = 

    # This amount per 100g?
    #round all macros up to the nearest gram - not doubles when calculating optimal meal?
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)
    fiber = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    #what other methods should we have?

    #need any "on save" methods?
    #eg convert from "1 spoonful" to value in grams

#---------------------------------------------

class Meal(models.Model):
    meal_id = models.CharField(max_length=20, blank=True, unique=True, default=uuid4)
    creator_id = models.CharField(max_length=120)
    meal_name = models.CharField(max_length=120)
    creation_date = models.DateTimeField(default=timezone.now())

    #list of foods that are in the meal AND the amount of that food that's included

    calories = models.IntegerField(null=True)
    protein = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    carbs = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    fiber = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    fat = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    #calculation goal for the meal for fats, protein, and carbs
    #cals, fats, protein, carbs allocated FOR THE MEAL
    #potentially add info for 'bounds' as in 'no more than 20oz chicken please'
    

    #mini model - holding only many to many relationship to foods, and 
    # also the proportion of food that will be in it
    #start serving size as null, will change once the food has been added in?
    #or does the class just hold on to these values and work only with the food objects, then
    #come back and populate the meal object
    #because like, the algorithm needs to know the foods to be able to calculate the serving sizes


    def __str__(self):
        return self.meal_name

    class Meta:
        ordering = ['creation_date']


#---------------------------------------------

# MealItem objects are unique to their meals - even if several meals all contain
# 1 serving of chicken, new identical objects will be created for all of them
class MealItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT)
    food_item = models.ForeignKey(Food, on_delete=models.PROTECT, null=True, blank=True)
    #per 100g portion - this is what the USDA database provides for all entries
    food_proportion = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.id

#---------------------------------------------


class Day(models.Model):
    date = models.DateTimeField()
    #user id of user whose day this is
    num_of_meals = models.IntegerField()
    #array of meal objects

    def __str__(self):
        return self.id

