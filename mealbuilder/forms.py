from django import forms
from .models import Food, Meal, Plan

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
        fields = ('name',)


    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)

# class EventForm(ModelForm):
#   class Meta:
#     model = Event
#     # datetime-local is a HTML5 input type, format to make date time show on fields
#     widgets = {
#       'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#       'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#     }
#     fields = '__all__'
#
#   def __init__(self, *args, **kwargs):
#     super(EventForm, self).__init__(*args, **kwargs)
#     # input_formats to parse HTML5 datetime-local input to datetime field
#     self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
#     self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

class PlanNoneForm(ModelForm):
    plan = forms.ModelChoiceField(queryset=Plan.objects.all().order_by('create_date'))

    class Meta:
        model = Plan
        fields = ('plan',)

    def __init__(self, *args, **kwargs):
      super(PlanNoneForm, self).__init__(*args, **kwargs)

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        exclude=('field_count','profile','create_date','date','meal')

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
      super(PlanForm, self).__init__(*args, **kwargs)
      hi
=======
        id = kwargs.pop('id', None)
        super().__init__(*args, **kwargs)
        if id:
            meals = Plan.objects.get(pk=id).meal.all()
        else:
            try:
                meals = self.instance.meal.all()
            except:
                meals = set()
        for i in range(len(meals)):
            field_name = 'meal_%s' % (i+1,)
            self.fields[field_name] = forms.ModelChoiceField(queryset=Meal.objects.all(),required=False)
            self.fields[field_name].label = "Meal"
            try:
                self.initial[field_name] = meals[i].id
            except IndexError:
                self.initial[field_name] = None
        # create an extra blank field
        if len(meals) == 0:
            field_name = 'meal_1'
            self.fields[field_name] = forms.ModelChoiceField(queryset=Meal.objects.all())
            self.fields[field_name].label = "Meal"
>>>>>>> master

    def clean(self):
        meals = set()
        i = 1
        field_name = 'meal_%s' % (i,)
        while self.cleaned_data.get(field_name):
            meal = self.cleaned_data[field_name]
            if meal in meals:
                self.add_error(field_name, 'Duplicate')
            else:
                meals.add(meal)
            i += 1
            field_name = 'meal_%s' % (i,)
        self.cleaned_data["meals"] = meals

    def get_meal_fields(self):
        for field_name in self.fields:
            if field_name.startswith('meal_'):
                yield self[field_name]

    def get_other_fields(self):
        for field_name in self.fields:
            if field_name.startswith('meal_'):
                pass
            else:
                yield self[field_name]
