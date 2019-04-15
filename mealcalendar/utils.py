
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from mealbuilder.models import Meal

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events, meals):
		events_per_day = events.filter(start_time__day=day)
		meals_per_day = meals.filter(creation_date__day=day)
		d = ''
		for event in events_per_day:
			d += '<li> {title} </li>'.format(title=event.get_html_url)

		for meal in meals_per_day:
			d += '<li> {name} </li>'.format(name=meal.meal_name)

		if day != 0:
			return "<td><span class='date'>{day}</span><ul> {d} </ul></td>".format(day=day,d=d)
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events, meals):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events, meals)
		return '<tr> {week} </tr>'.format(week=week)

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
		meals = Meal.objects.filter(creation_date__year=self.year, creation_date__month=self.month)

		cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += '{formatmonthname}\n'.format(formatmonthname=self.formatmonthname(self.year, self.month, withyear=withyear))
		cal += '{formatweekheader}\n'.format(formatweekheader=self.formatweekheader())
		for week in self.monthdays2calendar(self.year, self.month):
			cal += '{formatweek}\n'.format(formatweek=self.formatweek(week, events, meals))
		return cal
