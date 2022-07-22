from django.db import models
from django.contrib.auth.models import User
from app_users.models import Profile
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
	"""Модель Статус задачи"""
	title = models.CharField(max_length=20, verbose_name=_('наименование'))

	def __str__(self):
		return self.title


class Task(models.Model):
	"""Модель Задача"""
	title = models.TextField(max_length=300, db_index=True, verbose_name=_('наименование'))
	responsible = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE, verbose_name=_('ответственный'))
	date_from = models.DateField(auto_now_add=True, db_index=True, verbose_name=_('дата создания'))
	date_date_to = models.DateField(db_index=True, verbose_name=_('дедлайн'))
	status = models.ForeignKey(Status, default=1, db_index=True, on_delete=models.CASCADE, verbose_name=_('статус'))
	published = models.BooleanField(default=True, verbose_name=_('видимость'))

	def __str__(self):
		return self.title


class Comment(models.Model):
	"""Модель Комментарий"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	descr = models.TextField(max_length=300, verbose_name=_('комментарий'))

	def __str__(self):
		return self.descr