from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .models import Task, Comment
import datetime

class AddTaskForm(forms.ModelForm):
	date_date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                     initial=format(datetime.date.today(),'%Y-%m-%d'), localize=True)
	class Meta:
		model = Task
		fields = ['id', 'title', 'responsible', 'date_date_to', 'status', 'published']


class AddCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['descr']


class UpdateTaskForm(forms.ModelForm):
	date_date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'))
	class Meta:
		model = Task
		fields = ['id', 'title', 'responsible', 'date_date_to', 'status', 'published']


class FilterForm(forms.Form):
	task_filter = forms.CharField(max_length=100, help_text='фильтр')
