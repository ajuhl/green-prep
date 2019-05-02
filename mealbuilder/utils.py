
from datetime import datetime, timedelta
from calendar import HTMLCalendar, _localized_month
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
				return '<td class="fc-day fc-widget-content" ondblclick="goToPlan({date})"><span class="date">{day}</span><ul> {d} </ul></td>'.format(date=date,day=day,d=d)
			return '<td></td>'
		if day != 0:
			return '<td class="fc-day fc-widget-content" ondblclick="goToDate({date})"><span class="date">{day}</span><ul> {d} </ul></td>'.format(date=date,day=day,d=d)
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d)
		return '<tr class="fc-week"> {week} </tr>'.format(week=week)

	def formatweekheader(self):
		s = ''.join(self.formatweekday(i) for i in self.iterweekdays())
		return '<tr class="fc-first fc-last">%s</tr>' % s

	def formatmonthname(self, theyear, themonth, withyear=True):
		month_name = _localized_month('%B')
		if withyear:
			s = '%s %s' % (month_name[themonth], theyear)
		else:
			s = '%s' % month_name[themonth]

		prev_month = '<tr class="fc-header"><th colspan="2" class="fc-header-left"><span class="fc-button fc-button-prev fc-state-default fc-corner-left" unselectable="on" onclick="get_prev()"><span class="fc-text-arrow"><</span></span></th>'
		title = '<th colspan="3" class="fc-header-center"><span class="fc-header-title"><h2>%s</h2></span></th>' % s
		next_month = '<th colspan="2" class="fc-header-right"><span class="fc-button fc-button-next fc-state-default fc-corner-right" unselectable="on" onclick="get_next()"><span class="fc-text-arrow">></span></span></th></tr>'
		return prev_month+title+next_month


	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += '{formatmonthname}\n'.format(formatmonthname=self.formatmonthname(self.year, self.month, withyear=withyear))
		cal += '{formatweekheader}\n'.format(formatweekheader=self.formatweekheader())
		for week in self.monthdays2calendar(self.year, self.month):
			cal += '{formatweek}\n'.format(formatweek=self.formatweek(week))
		return cal
