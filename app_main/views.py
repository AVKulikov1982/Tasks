from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from app_tasks.models import Task
from app_tasks.forms import FilterForm
from app_tasks.api import check_deadline
import logging

logger = logging.getLogger(__name__)

# def valid_filter(t_filter, title):
# 	a = fuzz.token_sort_ratio(t_filter, title)
# 	if a >= 50:
# 		return True
# 	return False


class MainView(View):
	"""Представление главной страницы"""
	@staticmethod
	def get(request):
		check_deadline()
		task_filter_form = FilterForm()
		tasks = Task.objects.all().select_related('responsible')
		return render(request, context={'tasks': tasks, 'task_filter_form': task_filter_form},
					  template_name='main.html')

	@staticmethod
	def post(request):
		task_filter_form = FilterForm(request.POST)
		if task_filter_form.is_valid():
			task_filter = task_filter_form.cleaned_data.get('task_filter')
			tasks = list(filter(lambda x: task_filter in x.title, Task.objects.all().select_related('responsible')))
			#tasks = list(filter(lambda x: valid_filter(task_filter, x.title), Task.objects.all().select_related('responsible')))

		return render(request, context={'tasks': tasks, 'task_filter_form': task_filter_form},
				  template_name='main.html')




