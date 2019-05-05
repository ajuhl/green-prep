from django import forms
from .models import Food, Meal, Plan
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms import ModelForm, DateInput

class MealForm(ModelForm):
    class Meta:
        model = Meal
        exclude = (
        'create_date',
        'food',
        'profile',
        'calories',
        'protein',
        'carbs',
        'total_fat',
        'fiber',
        'sodium',
        'potassium',
        'sugars',
        'magnesium',
        'cholesterol',
        'sat_fat',
        'trans_fat')

    def __init__(self, *args, **kwargs):
        id = kwargs.pop('meal_id', None)
        super().__init__(*args, **kwargs)
        if id:
            foods = Meal.objects.get(pk=id).food.all()
        else:
            try:
                foods = self.instance.food.all()
            except:
                foods = set()
        for i in range(len(foods)):
            field_name = 'food_%s' % (i+1,)
            self.fields[field_name] = forms.ModelChoiceField(queryset=Food.objects.all(),required=False)
            self.fields[field_name].label = "Food"
            try:
                self.initial[field_name] = foods[i].id
            except IndexError:
                self.initial[field_name] = None
        # create an extra blank field
        if len(foods) == 0:
            field_name = 'food_1'
            self.fields[field_name] = forms.ModelChoiceField(queryset=Food.objects.all())
            self.fields[field_name].label = "Food"

    def clean(self):
        foods = set()
        i = 1
        field_name = 'food_%s' % (i,)
        while self.cleaned_data.get(field_name):
            food = self.cleaned_data[field_name]
            if food in foods:
                self.add_error(field_name, 'Duplicate')
            else:
                foods.add(food)
            i += 1
            field_name = 'food_%s' % (i,)
        self.cleaned_data["foods"] = foods

    def get_foods_fields(self):
        for field_name in self.fields:
            if field_name.startswith('food_'):
                yield self[field_name]

    def get_other_fields(self):
        for field_name in self.fields:
            if field_name.startswith('food_'):
                pass
            else:
                yield self[field_name]

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
        exclude=(
                'create_date',
                'date',
                'meal',
                'profile',
                'calories',
                'protein',
                'carbs',
                'total_fat',
                'fiber',
                'sodium',
                'potassium',
                'sugars',
                'magnesium',
                'cholesterol',
                'sat_fat',
                'trans_fat')

    def __init__(self, *args, **kwargs):
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

        # self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     'name',
        #     Row(
        #         Column('protein_goal', css_class='form-group col-md-2 mb-0'),
        #         Column('carb_goal', css_class='form-group col-md-2 mb-0'),
        #         Column('fat_goal', css_class='form-group col-md-2 mb-0'),
        #         css_class='form-row'
        #     )

        # )

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
