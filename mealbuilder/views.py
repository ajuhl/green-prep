from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta, date
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils import timezone
import calendar
from dal import autocomplete



from .forms import MealForm, PlanForm, PlanNoneForm
from .models import Food, Meal, Plan, MealFood
from .simplex import OptimizeMeal
from .utils import Calendar


def food(request, food_id=None):
    instance = get_object_or_404(Food, pk=food_id)
    context = {'food' : instance}
    return render(request, 'food_view.html', context)

def meal(request, meal_id=None):
    instance = get_object_or_404(Meal, pk=meal_id)
    context = {
    'mealfoods' : instance.mealfoods.all(),
    'meal' : instance}
    return render(request, 'meal_view.html', context)

def meal_edit(request, meal_id=None, profile_id=2):
    instance = Meal()
    if meal_id:
        instance = get_object_or_404(Meal, pk=meal_id,profile_id=profile_id)
    else:
        instance = Meal(profile_id=profile_id)

    form = MealForm(request.POST or None, instance=instance, meal_id=meal_id)
    if request.method == 'POST' and form.is_valid():
        meal = form.save()
        meal.mealfoods.clear()
        foods = set()
        for field_name in request.POST:
            if field_name.startswith('food_'):
                food = request.POST.get(field_name)
                if food in foods:
                    pass
                else:
                    foods.add(food)
                    MealFood.objects.create(meal=meal, food=Food.objects.get(pk=food))
        servingSizes=OptimizeMeal(meal)
        i=0
        for mealfood in meal.mealfoods.all():
            mealfood.quantity = round(servingSizes[i,0]*100)
            mealfood.updateNutrients()
            mealfood.save()
            i += 1

        meal.updateNutrients()
        meal.save()

        for plan in meal.plans.all():
            plan.updateNutrients()
            plan.save()

        context = {
        'mealfoods' : meal.mealfoods.all(),
        'meal' : meal}
        return render(request, 'meal_view.html', context)
    else:
        error = form.errors
    return render(request, 'meal_edit.html', {'form': form, 'meal':instance, 'meal_id':meal_id})


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
        instance.updateNutrients()
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


def grocery_list(request, start_date=None, end_date=None):
    foods = set()
    gList={}
    plans = Plan.objects.all()
    for plan in plans:
        for meal in plan.meal.all():
            for mealfood in meal.mealfoods.all():
                name = mealfood.food.name
                if mealfood.food in foods:
                    gList[name] += mealfood.quantity
                else:
                    foods.add(mealfood.food)
                    gList[name] = mealfood.quantity

    context = {
    'gList' : gList,
    'start_date' : start_date,
    'end_date' : end_date}
    return render(request, 'grocery_list.html', context)

class FoodAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        qs = Food.objects.all()

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs
