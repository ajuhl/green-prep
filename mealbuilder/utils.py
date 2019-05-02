
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
				d += '<div class="fc-event fc-event-hori fc-event-draggable fc-event-start fc-event-end"><div class="fc-event-inner"><span class="fc-event-title">{name}</span></div></div>'.format(name=meal.name)
			if day != 0:
				return '<td class="fc-day fc-widget-content" ondblclick="goToPlan({date})"><div style="min-height: 106px;"><div class="fc-day-number">{day}</div><div class="fc-day-content"><div style="position: relative; height: 84px;">{d}</div></div</td>'.format(date=date,day=day,d=d)
			return '<td class="fc-day fc-widget-content"></td>'

		if day != 0:
			return '<td class="fc-day fc-widget-content" ondblclick="goToDate({date})"><div style="min-height: 106px;"><div class="fc-day-number">{day}</div><div class="fc-day-content"><div style="position: relative; height: 84px;">{d}</div></div</td>'.format(date=date,day=day,d=d)
		return '<td class="fc-day fc-widget-content"></td>'

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

		prev_month = '<table class="fc-header" style="width:100%"><tbody><tr><td class="fc-header-left"><span class="fc-button fc-button-prev fc-state-default fc-corner-left" unselectable="on" onclick="get_prev()"><span class="fc-text-arrow"><</span></span></td>'
		title = '<td class="fc-header-center"><span class="fc-header-title"><h2>%s</h2></span></td>' % s
		next_month = '<td class="fc-header-right"><span class="fc-button fc-button-next fc-state-default fc-corner-right" unselectable="on" onclick="get_next()"><span class="fc-text-arrow">></span></span></td></tr></tbody></table>'
		return prev_month+title+next_month


	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		cal = '<div id="wrap"><div id="calendar" class="fc fc-ltr">{formatmonthname}\n'.format(formatmonthname=self.formatmonthname(self.year, self.month, withyear=withyear))
		cal += '<div class="fc-view fc-view-month fc-grid" style="position: relative" unselectable="on"><table class="fc-border-separate" style="width:100%" cellspacing="0"><thead>{formatweekheader}</thead><tbody>\n'.format(formatweekheader=self.formatweekheader())
		for week in self.monthdays2calendar(self.year, self.month):
			cal += '{formatweek}\n'.format(formatweek=self.formatweek(week))
		return cal+'</tbody></table></div></div></div>'
