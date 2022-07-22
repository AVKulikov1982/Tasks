from .models import Task, Status
from django.contrib.auth.models import User
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
	"""Сериализатор модели Задача"""
	responsible = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
	# responsible_id = serializers.SlugRelatedField(slug_field='username',
	# 											  queryset=User.objects.all(),
	# 											  write_only=True,
    #     										  allow_null=True,)
	status = serializers.SlugRelatedField(slug_field='title', queryset=Status.objects.all())
	# # status_id = serializers.SlugRelatedField(slug_field='id',
	# 											  queryset=Status.objects.all().values('id'),
	# 											  write_only=True,
	# 											  allow_null=True, )


	class Meta:
		model = Task
		fields = ['id', 'title', 'responsible', 'date_from', 'date_date_to', 'status']
	#
	# def create(self, validated_data):
	# 	print(validated_data)
	# 	task = Task.objects.create(**validated_data)
	# 	return Task.objects.create(task=task)
	# #
	# def update(self, instance, validated_data):
	# 	instance.title = validated_data.get('title', instance.title)
	# 	instance.responsible = validated_data.get('responsible', instance.responsible)
	# 	instance.date_date_to = validated_data.get('date_date_to', instance.date_date_to)
	# 	instance.status = validated_data.get('status', instance.status)
	# 	instance.save()
	# 	self.send_message(instance)
	# 	return instance
	#
	# def send_message(self, data):
	# 	pass