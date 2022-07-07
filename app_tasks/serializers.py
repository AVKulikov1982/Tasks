from .models import Task
from django.contrib.auth.models import User
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
	responsible = serializers.StringRelatedField()
	status = serializers.StringRelatedField()

	class Meta:
		model = Task
		fields = ['id', 'title', 'responsible', 'date_from', 'date_date_to', 'status']


