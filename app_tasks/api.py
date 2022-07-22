import datetime

from django.contrib.auth.models import User
from .models import Task, Comment, Status
from .forms import AddCommentForm, UpdateTaskForm, FilterForm, AddTaskForm
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.db.models import Q


def check_deadline():
	"""Функция проверки даты окончания задачи и присвоения задаче соответствующего статуса """
	date = datetime.date.today()

	status = Status.objects.get(title='просрочена')
	task_for_update = Task.objects.filter(date_date_to__lt=date).filter(status=Status.objects.get(title='в работе'))
	for task in task_for_update:
		task.status = status
	Task.objects.bulk_update(task_for_update, ['status'])

	status = Status.objects.get(title='в работе')
	task_for_update = Task.objects.filter(date_date_to__gt=date).filter(status=Status.objects.get(title='просрочена'))
	for task in task_for_update:
		task.status = status
	Task.objects.bulk_update(task_for_update, ['status'])


class TaskList(ModelViewSet):
	"""Представление списка задач в зависимости от запроса (get, post, put, delete)."""
	serializer_class = TaskSerializer

	queryset = Task.objects.all()
	permission_classes_by_action = {'create': [IsAuthenticated],
									'list': [IsAuthenticated],
									'retrieve': [IsAuthenticated],
									'update': [IsAuthenticated],
									'destroy': [IsAdminUser],
									}
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['responsible', 'status']
#	ordering_fields = ['title', 'responsible', 'date_from', 'date_date_to', 'status']
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'main.html'

	def list(self, request, *args, **kwargs):
		check_deadline()
		task_filter_form = FilterForm()
		queryset = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(queryset, many=True)
		return Response({'tasks': serializer.data, 'task_filter_form': task_filter_form}, template_name='main.html')

	def get(self, request, *args, **kwargs):
		check_deadline()
		task_filter_form = FilterForm()
		comment_form = AddCommentForm()
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		comments = Comment.objects.filter(task_id=instance.id).select_related('user')
		responsibles = User.objects.all().values('id', 'username')
		return Response({'task': serializer.data, 'comment_form': comment_form, 'comments':comments,
						 'responsibles': responsibles, 'task_filter_form': task_filter_form}, template_name='task.html')

	def create(self, request, *args, **kwargs):
		task_form = AddTaskForm(request.POST)
		task_filter_form = FilterForm()
		if task_form.is_valid():
			title = task_form.cleaned_data.get('title')
			responsible = task_form.cleaned_data.get('responsible')
			date_date_to = task_form.cleaned_data.get('date_date_to')
			status = task_form.cleaned_data.get('status')
			Task.objects.create(title=title, responsible=responsible, date_date_to=date_date_to, status=status)
		# serializer = self.get_serializer(data=request.POST)
		# serializer.is_valid(raise_exception=True)
		# self.perform_create(serializer)
		# headers = self.get_success_headers(serializer.data)
		tasks = Task.objects.all().select_related('responsible')
		return Response({'tasks': tasks, 'task_filter_form': task_filter_form}, template_name='main.html')

	def update(self, request, *args, **kwargs):
		task_filter_form = FilterForm()
		pk = kwargs['pk']
		instance = self.get_object()
		task_form_update = UpdateTaskForm(request.POST)
		task = Task.objects.get(id=pk)
		comments = Comment.objects.filter(task_id=instance.id).select_related('user')
		responsibles = User.objects.all().values('id', 'username')
		comment_form = AddCommentForm()
		if task_form_update.is_valid():
			task.title = task_form_update.cleaned_data.get('title')
			task.responsible = task_form_update.cleaned_data.get('responsible')
			task.date_date_to = task_form_update.cleaned_data.get('date_date_to')
			task.status = task_form_update.cleaned_data.get('status')
			task.save()
			Comment.objects.create(user=request.user, task=task, descr=f'редактирование задачи')
			return Response({'task': task, 'comment_form': comment_form,
							 'comments': comments, 'responsibles': responsibles, 'task_filter_form': task_filter_form},
							template_name='task.html')

	def get_permissions(self):
		try:
			# return permission_classes depending on `action`
			return [permission() for permission in self.permission_classes_by_action[self.action]]
		except KeyError:
			# action is not set return default permission_classes
			return [permission() for permission in self.permission_classes]

