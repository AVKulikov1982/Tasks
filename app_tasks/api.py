from django.contrib.auth.models import User
from .models import Task
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


class TaskList(ModelViewSet):
	serializer_class = TaskSerializer
	queryset = Task.objects.all()
	permission_classes_by_action = {'create': [IsAuthenticated],
									'list': [IsAuthenticated],
									'retrieve': [IsAuthenticated],
									'update': [IsAuthenticated],
									'destroy': [IsAdminUser],
									}
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	ordering_fields = ['title', 'responsible', 'date_from', 'date_date_to', 'status']

	def get_permissions(self):
		try:
			# return permission_classes depending on `action`
			return [permission() for permission in self.permission_classes_by_action[self.action]]
		except KeyError:
			# action is not set return default permission_classes
			return [permission() for permission in self.permission_classes]
