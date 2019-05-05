from django.urls import path, include
from mealbuilder import views as mealbuilder_views

urlpatterns = [
    path('', mealbuilder_views.meal_edit, name='meal'),
    path('(<meal_id>)', mealbuilder_views.meal, name='meal_view'),
    path('calendar', mealbuilder_views.CalendarView.as_view(), name='calendar'),
    path('', mealbuilder_views.plan, name='plan'),
    path('new/', mealbuilder_views.meal_edit, name='meal_new'),
    path('edit/(<meal_id>)/', mealbuilder_views.meal_edit, name='meal_edit'),
    path('plan/(<date>)', mealbuilder_views.plan_view, name='plan_view'),
    path('plan/new/', mealbuilder_views.plan, name='plan_new'),
    path('plan/edit/(<date>)', mealbuilder_views.plan, name='plan_edit'),
    path('plan/edit/', mealbuilder_views.plan, name='plan_edit'),
    path('plan/edit/(<date>)/(<id>)', mealbuilder_views.plan, name='plan_edit'),
    path('plan/none/(<date>)', mealbuilder_views.plan_none, name='plan_none'),
    path('grocerylist/', mealbuilder_views.grocery_list, name='grocery_list'),
    path('grocerylist/(<start_date>)/(<end_date>)', mealbuilder_views.grocery_list, name='grocery_list'),
]
