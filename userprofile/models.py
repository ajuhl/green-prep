from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    # Personal Info
    #user_id - is username enough? if not we can generate an id
    user_id = 1
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birthdate = models.DateField(null=True, blank=True)
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    # Height stored in cm?
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # Weight stored in kg?
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    #display preferences
    #measurements - metric/imperial
    #display foods in per 100g or home serving

    # Activity Level and Macro Calculation Info
    LIGHTLY_ACTIVE = 1
    MODERATELY_ACTIVE = 2
    VERY_ACTIVE = 3
    EXTRA_ACTIVE = 4
    ACTIVITY_LEVEL = (
        (LIGHTLY_ACTIVE, 'Lightly Active'),
        (MODERATELY_ACTIVE, 'Moderately Active'),
        (VERY_ACTIVE, 'Very Active'),
        (EXTRA_ACTIVE, 'Extra Active'),
    )
    activity_level = models.PositiveSmallIntegerField(choices=ACTIVITY_LEVEL, null=True, blank=True)

    FAT_LOSS = 1
    MAINTENENCE = 2
    MUSCLE_GAIN = 3
    PHYSICAL_GOAL = (
        (FAT_LOSS, 'Fat Loss'),
        (MAINTENENCE, 'Maintenence'),
        (MUSCLE_GAIN, 'Muscle Gain'),
    )
    physical_goal = models.PositiveSmallIntegerField(choices=PHYSICAL_GOAL, null=True, blank=True)

    # bools for all the nutrients - do you want to view them by default?
    # array of enabled nutrients

    #METHODS - calculate by default, but allow user input
    #upon updates to other parts, don't change this without getting clear consent
    p_goal = models.IntegerField(null=True, blank=True)
    c_goal = models.IntegerField(null=True, blank=True)
    f_goal = models.IntegerField(null=True, blank=True)

    #list of their hearted meal objects that they want to go back to
    #list of hearted day plans (which are lists of meal objects)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
