from django.urls import path,include
from mealcalendar import views as mealcalendar_views

app_name = 'mealcalendar'
urlpatterns = [
    path('', mealcalendar_views.CalendarView.as_view(), name='mealcalendar'),
    path('event/new/', mealcalendar_views.event, name='event_new'),
    path('event/edit/(<start_time>)/', mealcalendar_views.event, name='event_edit'),
]
