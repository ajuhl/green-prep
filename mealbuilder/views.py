from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta, date
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils import timezone
import calendar


from .forms import MealForm, PlanForm, PlanNoneForm
from .models import Food, Meal, Plan, MealFood
from .simplex import OptimizeMeal
from .utils import Calendar

def meal(request, meal_id=None):
    instance = get_object_or_404(Meal, pk=meal_id)
    context = {
    'mealfoods' : instance.mealfoods.all(),
    'meal' : instance}
    return render(request, 'meal_view.html', context)

def meal_edit(request, meal_id=None):
    instance = Meal()
    if meal_id:
        instance = get_object_or_404(Meal, pk=meal_id)
    else:
        instance = Meal()

    form = MealForm(request.POST or None, instance=instance, meal_id=meal_id)
    if request.method == 'POST' and form.is_valid():
        meal = form.save()
        meal.food.clear()
        foods = set()
        for field_name in request.POST:
            if field_name.startswith('food_'):
                food = request.POST.get(field_name)
                if food in foods:
                    pass
                else:
                    foods.add(food)
                    MealFood.objects.create(meal=meal, food=Food.objects.get(pk=food))
        context = {
        'mealfoods' : meal.mealfoods.all(),
        'meal' : meal}
        return render(request, 'meal_view.html', context)
    else:
        error = form.errors
    return render(request, 'meal_edit.html', {'form': form, 'meal':instance, 'meal_id':meal_id})

# def meal(request):
#
#     context = {
#         'message': 'Hello, world. You\'re at the mealbuilder index.',
#     }
#
#     if request.method == 'POST':
#         form = MealForm(request.POST)
#         if form.is_valid():
#             meal = CreateMeal(form)
#             optimized_meal = OptimizeMeal(meal)
#             context.update({
#                 'optimized_meal': meal,
#                 'message': meal.name + " successfully created",
#             })
#
#     else:
#         form = MealForm()
#
#     context.update({
#         'form': form,
#     })
#     return render(request, 'mealbuilder.html', context=context)


def CreateMeal(form):
    meal = Meal(
        name = form.cleaned_data.get('name'),
        protein_goal = form.cleaned_data.get('protein_goal'),
        carb_goal = form.cleaned_data.get('carb_goal'),
        fat_goal = form.cleaned_data.get('fat_goal')
    )
    meal.save()

    meal_item_1 = meal.mealfoods.create(
        food = form.cleaned_data.get('food_1'),
        limit = form.cleaned_data.get('food_1_limit')
    )
    meal_item_1.save()


    meal_item_2 = meal.mealfoods.create(
        food = form.cleaned_data.get('food_2'),
        limit = form.cleaned_data.get('food_2_limit')
    )
    meal_item_2.save()

    return meal

class CalendarView(generic.ListView):
    model = Plan
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def plan_view(request, date=None):
    instance = get_object_or_404(Plan, date=date)
    context = {
    'meals' : instance.meal.all(),
    'plan' : instance,
    'date' : date}
    return render(request, 'plan_view.html', context)

def plan(request, date=None, id=None):
    instance = Plan()
    if date:
        if id:
            instance = Plan.objects.get(pk=id)
            instance.pk = None
            instance.date = date
            instance.create_date = timezone.now()
            instance.name = '{name}-COPY'.format(name=instance.name)
        else:
            try:
                instance = Plan.objects.get(date=date)
            except Plan.DoesNotExist:
                instance = Plan(date=date, create_date=timezone.now())
    else:
        instance = Plan()
    form = PlanForm(request.POST or None, instance=instance, id=id)
    if request.method == 'POST' and form.is_valid():
        plan = form.save()
        plan.meal.clear()
        meals = set()
        for field_name in request.POST:
            if field_name.startswith('meal_'):
                meal = request.POST.get(field_name)
                if meal in meals:
                    pass
                else:
                    meals.add(meal)
                    plan.meal.add(Meal.objects.get(pk=meal))
        instance = get_object_or_404(Plan, date=date)
        context = {
        'meals' : instance.meal.all(),
        'plan' : instance,
        'date' : date}
        return render(request, 'plan_view.html', context)
    else:
        error = form.errors
    return render(request, 'plan.html', {'form': form, 'date':date, 'id':id})

def plan_none(request, date=None):
    return render(request, 'plan_none.html', {'plans':Plan.objects.all(), 'date': date})
