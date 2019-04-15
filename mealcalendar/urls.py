from django.urls import path,include
from . import views

app_name = 'mealcalendar'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='mealcalendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/(<event_id>)/', views.event, name='event_edit'),
    path('meal/new/', views.meal, name='meal_new'),
    path('meal/edit/(<meal_id>)/', views.meal, name='meal_edit'),
]
