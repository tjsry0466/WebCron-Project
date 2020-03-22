from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        exclude = ('user', 'minute', 'day', 'week', 'month', 'dayoftheweek')
        fields = '__all__'