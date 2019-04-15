
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from mealbuilder.simplex import OptimizeMeal

from .models import *
from mealbuilder.models import Meal
from .utils import Calendar
from .forms import EventForm
from mealbuilder.forms import MealBuilderForm


class CalendarView(generic.ListView):
    model = Event
    template_name = 'mealcalendar/calendar.html'

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

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('mealcalendar:mealcalendar'))
    return render(request, 'mealcalendar/event.html', {'form': form})


def meal(request, meal_id=None):
    context = {
        'message': 'Hello, world. You\'re at the mealbuilder index.',
    }
    instance = Meal()
    if meal_id:
        instance = get_object_or_404(Event, pk=meal_id)
    else:
        instance = Meal()

    form = MealBuilderForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        meal = CreateMealFromFormData(form)
        optimized_meal = OptimizeMeal(meal)
        context.update({
            'optimized_meal': meal,
            'message': meal.meal_name + " successfully created",
        })
        return HttpResponseRedirect(reverse('mealcalendar:mealcalendar'))
    return render(request, 'mealcalendar/mealbuilder.html', {'form': form})


def CreateMealFromFormData(form):
    meal = Meal(
        meal_name = form.cleaned_data.get('meal_name'),
        protein_goal = form.cleaned_data.get('protein_goal'),
        carb_goal = form.cleaned_data.get('carb_goal'),
        fat_goal = form.cleaned_data.get('fat_goal')
    )
    meal.save()

    meal_item_1 = meal.mealitem_set.create(
        food = form.cleaned_data.get('food_1'),
        limit = form.cleaned_data.get('food_1_limit')
    )
    meal_item_1.save()


    meal_item_2 = meal.mealitem_set.create(
        food = form.cleaned_data.get('food_2'),
        limit = form.cleaned_data.get('food_2_limit')
    )
    meal_item_2.save()

    return meal
