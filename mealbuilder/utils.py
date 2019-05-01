
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Meal, Plan

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day):
		d = ''
		date = "'{year}-{month}-{day}'".format(year=self.year,month=self.month,day=day)
		try:
			plan = Plan.objects.get(date__year=self.year, date__month=self.month, date__day=day)
		except Plan.DoesNotExist:
			plan = None
		if plan is not None:
			meals = plan.meal.all()

			for meal in meals:
				d += '<li> {name} </li>'.format(name=meal.name)
			if day != 0:
				return '<td ondblclick="goToPlan({date})"><span class="date">{day}</span><ul> {d} </ul></td>'.format(date=date,day=day,d=d)
			return '<td></td>'
		if day != 0:
			return '<td ondblclick="goToDate({date})"><span class="date">{day}</span><ul> {d} </ul></td>'.format(date=date,day=day,d=d)
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d)
		return '<tr> {week} </tr>'.format(week=week)

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += '{formatmonthname}\n'.format(formatmonthname=self.formatmonthname(self.year, self.month, withyear=withyear))
		cal += '{formatweekheader}\n'.format(formatweekheader=self.formatweekheader())
		for week in self.monthdays2calendar(self.year, self.month):
			cal += '{formatweek}\n'.format(formatweek=self.formatweek(week))
		return cal
