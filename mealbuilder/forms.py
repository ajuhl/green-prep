from django import forms
from .models import Food, Meal, Event, Plan

from django.forms import ModelForm, DateInput

class MealForm(ModelForm):

    protein_goal = forms.IntegerField(initial=50) #this will be initialized from day goalMacros
    carb_goal = forms.IntegerField(initial=30)
    fat_goal = forms.IntegerField(initial=20)
    food_1 = forms.ModelChoiceField(queryset=Food.objects.all().order_by('name'))
    food_1_limit = forms.IntegerField(required=False)
    food_2 = forms.ModelChoiceField(queryset=Food.objects.all().order_by('name'))
    food_2_limit = forms.IntegerField(required=False)

    class Meta:
        model = Meal
        fields = ('name','profile')


    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields='__all__'

    def __init__(self, *args, **kwargs):
      super(PlanForm, self).__init__(*args, **kwargs)

class PlanNoneForm(forms.Form):
    plan = forms.ModelChoiceField(queryset=Plan.objects.all().order_by('create_date'))
