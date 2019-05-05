from django.db import models
from django.urls import reverse
from django.utils import timezone
from uuid import uuid4
import datetime
import math

from userprofile.models import Profile

# Create your models here.

class Food(models.Model):
    # db_num = models.CharField(max_length = 6)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length = 120)
    #serving_sizes(S)  =

    # This amount per 100g?
    #round all macros up to the nearest gram - not doubles when calculating optimal meal?
    calories = models.PositiveSmallIntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    total_fat = models.FloatField(default = 0)
    fiber = models.FloatField()
    sodium = models.FloatField(default = 0)
    potassium = models.FloatField(default = 0)
    sugars = models.FloatField(default = 0)
    magnesium = models.FloatField(default = 0)
    cholesterol = models.FloatField(default = 0)
    sat_fat = models.FloatField(default = 0)
    trans_fat = models.FloatField(default = 0)

    def __str__(self):
        return self.name

    #what other methods should we have?

    #need any "on save" methods?
    #eg convert from "1 spoonful" to value in grams

#---------------------------------------------

class Meal(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    create_date = models.DateTimeField(default=timezone.now())

    protein_goal = models.PositiveSmallIntegerField(null=True)
    carb_goal = models.PositiveSmallIntegerField(null=True)
    fat_goal = models.PositiveSmallIntegerField(null=True)

    food = models.ManyToManyField(Food, through='MealFood', related_name='meals')

    calories = models.PositiveSmallIntegerField(default=0)
    protein = models.PositiveSmallIntegerField(default=0)
    carbs = models.PositiveSmallIntegerField(default=0)
    total_fat = models.PositiveSmallIntegerField(default=0)
    fiber = models.PositiveSmallIntegerField(default=0)
    sodium = models.PositiveSmallIntegerField(default=0)
    potassium = models.PositiveSmallIntegerField(default=0)
    sugars = models.PositiveSmallIntegerField(default=0)
    magnesium = models.PositiveSmallIntegerField(default=0)
    cholesterol = models.PositiveSmallIntegerField(default=0)
    sat_fat = models.PositiveSmallIntegerField(default=0)
    trans_fat = models.PositiveSmallIntegerField(default=0)
    #calculation goal for the meal for fats, protein, and carbs
    #cals, fats, protein, carbs allocated FOR THE MEAL
    #potentially add info for 'bounds' as in 'no more than 20oz chicken please'


    #mini model- holding only many to many relationship to foods, and
    # also the portion of food that will be in it
    #start serving size as null, will change once the food has been added in?
    #or does the class just hold on to these values and work only with the food objects, then
    #come back and populate the meal object
    #because like, the algorithm needs to know the foods to be able to calculate the serving sizes
    def get_html_url(self):
        url = reverse('mealcalendar:meal_edit', args=(self.id,))
        return '<a href="{url}"> {name} </a>'.format(url=url,name=self.name)

    def __str__(self):
        return self.name

    def updateNutrients(self):
        self.protein = 0
        self.carbs = 0
        self.total_fat = 0
        self.calories = 0
        self.fiber = 0
        self.sodium =0
        self.potassium = 0
        self.sugars = 0
        self.magnesium =0
        self.cholesterol = 0
        self.sat_fat = 0
        self.trans_fat =0

        for mealfood in self.mealfoods.all():
            quantity = mealfood.quantity/100
            self.protein = int(self.protein + mealfood.protein)
            self.carbs = int(self.carbs + mealfood.carbs)
            self.total_fat =int(self.total_fat + mealfood.fat)
            self.calories = int(round(self.calories +  (mealfood.food.calories * quantity)))
            self.fiber = int(round(self.fiber +  (mealfood.food.fiber * quantity)))
            self.sodium = int(round(self.sodium +  (mealfood.food.sodium * quantity)))
            self.potassium = int(round(self.potassium +  (mealfood.food.potassium * quantity)))
            self.sugars = int(round(self.sugars +  (mealfood.food.sugars * quantity)))
            self.magnesium = int(round( self.magnesium +  (mealfood.food.magnesium * quantity)))
            self.cholesterol = int(round(self.cholesterol +  (mealfood.food.cholesterol * quantity)))
            self.sat_fat = int(round(self.sat_fat +  (mealfood.food.sat_fat * quantity)))
            self.trans_fat = int(round(self.trans_fat +  (mealfood.food.trans_fat * quantity)))
            self.save()

    class Meta:
        ordering = ['create_date']




#---------------------------------------------

# MealItem objects are unique to their meals - even if several meals all contain
# 1 serving of chicken, new identical objects will be created for all of them
class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='mealfoods',null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='mealfoods',null=True, blank=True)
    #per 100g portion - this is what the USDA database provides for all entries
    quantity = models.PositiveSmallIntegerField(null=True)
    limit = models.PositiveSmallIntegerField(null=True)
    protein = models.PositiveSmallIntegerField(null=True)
    carbs = models.PositiveSmallIntegerField(null=True)
    fat = models.PositiveSmallIntegerField(null=True)
    calories = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return str(self.food.name + " - " + self.meal.name + " - " + self.meal.profile.user.username)

    def updateNutrients(self):
        self.protein = int(round(self.food.protein * self.quantity/100))
        self.carbs = int(round(self.food.carbs * self.quantity/100))
        self.fat = int(round(self.food.total_fat * self.quantity/100))
        self.calories = int(round(self.food.calories * self.quantity/100))
        self.save()

#---------------------------------------------

class Plan(models.Model):
    date = models.DateField()
    create_date = models.DateTimeField(null=True)
    profile = models.ForeignKey(Profile,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True)

    protein_goal = models.PositiveSmallIntegerField()
    carb_goal = models.PositiveSmallIntegerField()
    fat_goal = models.PositiveSmallIntegerField()

    calories = models.PositiveSmallIntegerField(null=True)
    protein = models.PositiveSmallIntegerField(default=0)
    carbs = models.PositiveSmallIntegerField(default=0)
    total_fat = models.PositiveSmallIntegerField(default=0)
    fiber = models.PositiveSmallIntegerField(default=0)
    sodium = models.PositiveSmallIntegerField(default=0)
    potassium = models.PositiveSmallIntegerField(default=0)
    sugars = models.PositiveSmallIntegerField(default=0)
    magnesium = models.PositiveSmallIntegerField(default=0)
    cholesterol = models.PositiveSmallIntegerField(default=0)
    sat_fat = models.PositiveSmallIntegerField(default=0)
    trans_fat = models.PositiveSmallIntegerField(default=0)

    meal = models.ManyToManyField(Meal, related_name='plans', null=True)

    @property
    def get_html_url(self):
        url = reverse('mealcalendar:plan_edit', args=(self.id,))
        return '<a href="{url}"> {name} </a>'.format(url=url,title=self.name)

    def __str__(self):
        return self.name

    def updateNutrients(self):
        self.protein = 0
        self.carbs = 0
        self.total_fat = 0
        self.calories = 0
        self.fiber = 0
        self.sodium =0
        self.potassium = 0
        self.sugars = 0
        self.magnesium =0
        self.cholesterol = 0
        self.sat_fat = 0
        self.trans_fat =0

        for meal in self.meal.all():
            self.protein = round(self.protein + meal.protein)
            self.carbs = round(self.carbs + meal.carbs)
            self.total_fat = round(self.total_fat + meal.total_fat)
            self.calories = round(self.calories +  meal.calories)
            self.fiber = round(self.fiber +  meal.fiber)
            self.sodium = round(self.sodium +  meal.sodium)
            self.potassium = round(self.potassium + meal.potassium)
            self.sugars = round(self.sugars +  meal.sugars)
            self.magnesium =round( self.magnesium + meal.magnesium)
            self.cholesterol = round(self.cholesterol + meal.cholesterol)
            self.sat_fat = round(self.sat_fat + meal.sat_fat)
            self.trans_fat = round(self.trans_fat + meal.trans_fat)
            self.save()
