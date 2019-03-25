from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=120)
    #serving_sizes(S)  =

    # This amount per 100g?
    #round all macros up to the nearest gram - not doubles
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)

    def _str_(self):
        return self.name

    #what other methods should we have?

    #need any "on save" methods?

#---------------------------------------------

class Meal(models.Model):
    #id =
    #id of user who created it
    #name of meal
    creation_date = models.DateTimeField(default=timezone.now())

    #list of foods that are in the meal AND the amount of that food that's included

    #calculation goal for the meal for fats, protein, and carbs
    #cals, fats, protein, carbs allocated FOR THE MEAL
    #potentially add info for 'bounds' as in 'no more than 20oz chicken please'


    #mini model - holding only many to many relationship to foods, and
    # also the proportion of food that will be in it
    #start serving size as null, will change once the food has been added in?
    #or does the class just hold on to these values and work only with the food objects, then
    #come back and populate the meal object
    #because like, the algorithm needs to know the foods to be able to calculate the serving sizes


    def _str_(self):
        return self.id

    class Meta:
        ordering = ['creation_date']


#---------------------------------------------


class Day(models.Model):
    #date
    #user id of user whose day this is
    #number of meals
    #array of meal objects

    def _str_(self):
        return self.id
