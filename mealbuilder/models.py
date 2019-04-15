from django.db import models
from django.utils import timezone
from uuid import uuid4
import datetime

# Create your models here.

class Food(models.Model):
    db_num = models.CharField(max_length = 6)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length = 120)
    #serving_sizes(S)  =

    # This amount per 100g?
    #round all macros up to the nearest gram - not doubles when calculating optimal meal?
    calories = models.IntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    # fiber = models.DecimalField( decimal_places=2)
    fat = models.FloatField()

    def __str__(self):
        return self.name

    #what other methods should we have?

    #need any "on save" methods?
    #eg convert from "1 spoonful" to value in grams

#---------------------------------------------

class Meal(models.Model):
    creator_id = models.CharField(max_length=120)
    meal_name = models.CharField(max_length=120)
    creation_date = models.DateTimeField(default=timezone.now())

    #list of foods that are in the meal AND the amount of that food that's included

    calories = models.IntegerField(null=True)
    protein = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    fiber = models.FloatField(null=True)
    fat = models.FloatField(null=True)

    protein_goal = models.IntegerField(null=True)
    carb_goal = models.IntegerField(null=True)
    fat_goal = models.IntegerField(null=True)
    #calculation goal for the meal for fats, protein, and carbs
    #cals, fats, protein, carbs allocated FOR THE MEAL
    #potentially add info for 'bounds' as in 'no more than 20oz chicken please'


    #mini model rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr- holding only many to many relationship to foods, and
    # also the portion of food that will be in it
    #start serving size as null, will change once the food has been added in?
    #or does the class just hold on to these values and work only with the food objects, then
    #come back and populate the meal object
    #because like, the algorithm needs to know the foods to be able to calculate the serving sizes
    def get_html_url(self):
        url = reverse('mealcalendar:meal_edit', args=(self.id,))
        return '<a href="{url}"> {name} </a>'.format(url=url,name=self.meal_name)

    def __str__(self):
        return self.meal_name

    def updateNutrients(self):
        self.protein = 0
        self.carbs = 0
        self.fat = 0
        self.calories = 0

        for item in self.mealitem_set.all():
            self.protein = self.protein + item.protein
            self.carbs = self.carbs + item.carbs
            self.fat = self.fat + item.fat
            self.calories = self.calories + item.calories
            self.save()

    class Meta:
        ordering = ['creation_date']


#---------------------------------------------

# MealItem objects are unique to their meals - even if several meals all contain
# 1 serving of chicken, new identical objects will be created for all of them
class MealItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    #per 100g portion - this is what the USDA database provides for all entries
    quantity = models.FloatField(null=True)
    limit = models.IntegerField(null=True)
    protein = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    calories = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)

    def updateNutrients(self):
        self.protein = self.food.protein * self.quantity
        self.carbs = self.food.carbs * self.quantity
        self.fat = self.food.fat * self.quantity
        self.calories = self.food.calories * self.quantity
        self.save()

#---------------------------------------------


class Day(models.Model):
    date = models.DateTimeField()
    #user id of user whose day this is
    num_of_meals = models.IntegerField()
    #array of meal objects

    def __str__(self):
        return self.id
