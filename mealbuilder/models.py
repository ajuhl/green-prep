from django.db import models
from django.urls import reverse
from django.utils import timezone
from uuid import uuid4
import datetime

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
    total_fat = models.FloatField(default = -1)
    fiber = models.FloatField()
    sodium = models.FloatField(default = -1)
    potassium = models.FloatField(default = -1)
    sugars = models.FloatField(default = -1)
    magnesium = models.FloatField(default = -1)
    cholesterol = models.FloatField(default = -1)
    sat_fat = models.FloatField(default = -1)
    trans_fat = models.FloatField(default = -1)

    def __str__(self):
        return self.name

    #what other methods should we have?

    #need any "on save" methods?
    #eg convert from "1 spoonful" to value in grams

#---------------------------------------------

class Meal(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    creation_date = models.DateTimeField(default=timezone.now())

    protein_goal = models.PositiveSmallIntegerField(null=True)
    carb_goal = models.PositiveSmallIntegerField(null=True)
    fat_goal = models.PositiveSmallIntegerField(null=True)

    food = models.ManyToManyField(Food, through='MealFood', related_name='meals')

    calories = models.PositiveSmallIntegerField(null=True)
    protein = models.FloatField(default = -1)
    carbs = models.FloatField(default = -1)
    total_fat = models.FloatField(default = -1)
    fiber = models.FloatField(default = -1)
    sodium = models.FloatField(default = -1)
    potassium = models.FloatField(default = -1)
    sugars = models.FloatField(default = -1)
    magnesium = models.FloatField(default = -1)
    cholesterol = models.FloatField(default = -1)
    sat_fat = models.FloatField(default = -1)
    trans_fat = models.FloatField(default = -1)
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
        self.fat = 0
        self.calories = 0

        for mealfood in self.mealfoods.all():
            self.protein = self.protein + mealfood.protein
            self.carbs = self.carbs + mealfood.carbs
            self.fat = self.fat + mealfood.fat
            self.calories = self.calories + mealfood.calories
            self.fiber = self.fiber + mealfood.fiber
            self.sodium = self.sodium + mealfood.sodium
            self.potassium = self.potassium + mealfood.potassium
            self.sugars = self.sugars + mealfood.sugars
            self.magnesium = self.magnesium + mealfood.magnesium
            self.cholesterol = self.cholesterol + mealfood.cholesterol
            self.sat_fat = self.sat_fat + mealfood.sat_fat
            self.trans_fat = self.trans_fat + mealfood.trans_fat
            self.save()

    class Meta:
        ordering = ['creation_date']




#---------------------------------------------

# MealItem objects are unique to their meals - even if several meals all contain
# 1 serving of chicken, new identical objects will be created for all of them
class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='mealfoods',null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='mealfoods',null=True, blank=True)
    #per 100g portion - this is what the USDA database provides for all entries
    quantity = models.FloatField(null=True)
    limit = models.PositiveSmallIntegerField(null=True)
    protein = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    calories = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return str(self.food.name + " - " + self.meal.name + " - " + self.meal.profile.user.username)

    def updateNutrients(self):
        self.protein = self.food.protein * self.quantity
        self.carbs = self.food.carbs * self.quantity
        self.fat = self.food.total_fat * self.quantity
        self.calories = ceil(self.food.calories * self.quantity)
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
    protein_actual = models.FloatField(null=True)
    carb_actual = models.FloatField(null=True)
    fat_actual = models.FloatField(null=True)

    meal = models.ManyToManyField(Meal, related_name='plans')

    @property
    def get_html_url(self):
        url = reverse('mealcalendar:plan_edit', args=(self.id,))
        return '<a href="{url}"> {name} </a>'.format(url=url,title=self.name)

    def __str__(self):
        return self.name

class SavedMeal(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    creation_date = models.DateTimeField(default=timezone.now())

    food = models.ManyToManyField(Food, related_name='savedmeals')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['creation_date']

#---------------------------------------------

class SavedPlan(models.Model):
    create_date = models.DateTimeField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    meal = models.ManyToManyField(Meal, related_name='savedplans')

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('mealcalendar:event_edit', args=(self.id,))
        return '<a href="{url}"> {title} </a>'.format(url=url,title=self.title)

    def __str__(self):
        return self.title
