# cal/models.py

from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True)

    @property
    def get_html_url(self):
        url = reverse('mealcalendar:event_edit', args=(self.id,))
        return '<a href="{url}"> {title} </a>'.format(url=url,title=self.title)

    def __str__(self):
        return self.title
