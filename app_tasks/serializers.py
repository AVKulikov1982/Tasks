from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
	"""Сериализатор модели Животное"""
	class Meta:
		model = Task
		fields = ['id', 'title', 'responsible', 'date_from', 'date_date_to', 'status']