from django.db import models

class GroceryList(models.Model):
    #grocery list id
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)

    #user id of user whose calendar this is
    #many to many of days for the dates of this period
    #start date
    #end date
    #calculated number of days
    #add up the servings of the foods in the meals in the days
    
    def _str_(self):
        return self.id