from django.urls import path, include
from mealbuilder import views as mealbuilder_views

urlpatterns = [
    path('', mealbuilder_views.meal, name='meal'),
    path('calendar', mealbuilder_views.CalendarView.as_view(), name='calendar'),
    path('', mealbuilder_views.plan, name='plan'),
    path('new/', mealbuilder_views.meal, name='meal_new'),
    path('edit/(<name>)/', mealbuilder_views.meal, name='meal_edit'),
    path('plan/new/', mealbuilder_views.plan, name='plan_new'),
    path('plan/edit/(<date>)', mealbuilder_views.plan, name='plan_edit'),
    path('plan/edit/', mealbuilder_views.plan, name='plan_edit'),
    path('plan/none/(<date>)', mealbuilder_views.plan_none, name='plan_none'),
]
