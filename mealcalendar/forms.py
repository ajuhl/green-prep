
from django.forms import ModelForm, DateInput
from mealcalendar.models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      'end_time': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%d',)
    self.fields['end_time'].input_formats = ('%Y-%m-%d',)
