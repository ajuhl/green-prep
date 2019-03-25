from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthdate', 'sex', 'height', 'weight', 'activity_level', 'physical_goal')
