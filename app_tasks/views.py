from django.contrib.auth.models import User
from app_users.models import Profile
from django.shortcuts import render, redirect
from django.views import View
from .models import Task, Comment, Status
from .forms import AddTaskForm, AddCommentForm, UpdateTaskForm, FilterForm
from django.http import HttpResponseBadRequest, HttpResponseForbidden


class AddTask(View):

	@staticmethod
	def get(request):
		task_form = AddTaskForm()
		task_filter_form = FilterForm()
		if request.user.is_authenticated:
			return render(request, 'add_task.html', context={'task_form': task_form, 'task_filter_form': task_filter_form})
		else:
			return HttpResponseBadRequest('войдите или зарегистрируйтесь')


class AddComment(View):

	@staticmethod
	def post(request, pk):
		if request.user.is_authenticated:
			comment_form = AddCommentForm(request.POST)
			if comment_form.is_valid():
				user = request.user
				task = Task.objects.get(id=pk)
				descr = comment_form.cleaned_data.get('descr')
				Comment.objects.create(user=user, task=task, descr=descr)
			return redirect(f'/api/tasks/{pk}')
		else:
			return HttpResponseBadRequest('войдите или зарегистрируйтесь')

class StopTask(View):

	@staticmethod
	def get(request, pk):
		if request.user.is_authenticated:
			task = Task.objects.get(id=pk)
			task.status = Status.objects.filter(title='закрыта')[0]
			task.published = False
			task.save()
			Comment.objects.create(user=request.user, task=task, descr='задачу закрыл')
			return redirect('/api/tasks/')
		else:
			return HttpResponseBadRequest('войдите или зарегистрируйтесь')


class ChangeResponsible(View):

	@staticmethod
	def post(request, pk):
		if request.user.is_authenticated:
			try:
				if request.POST['responsible']:
					task = Task.objects.get(id=pk)
					user = User.objects.get(id=int(request.POST['responsible']))
					task.responsible = user
					task.save()
					Comment.objects.create(user=request.user, task=task, descr=f'сменил ответственного на {task.responsible}')
			except:
				return HttpResponseBadRequest('что-то пошло не так')
			return redirect(f'/api/tasks/{pk}')
		else:
			return HttpResponseBadRequest('войдите или зарегистрируйтесь')


class UpdateTask(View):

	@staticmethod
	def get(request, pk):
		task_filter_form = FilterForm()

		if request.user.is_authenticated:
			task = Task.objects.get(id=pk)
			print(task.date_date_to)
			task_form_update = UpdateTaskForm(instance=task)
			return render(request, 'update_task.html', context={'task_form_update': task_form_update, 'pk': pk, 'task_filter_form': task_filter_form})
		else:
			return HttpResponseBadRequest('войдите или зарегистрируйтесь')