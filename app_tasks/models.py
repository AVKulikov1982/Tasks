from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
#	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, verbose_name=_('наименование'))
	responsible = models.ForeignKey(User, on_delete=models.CASCADE)
	date_from = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'))
	date_date_to = models.DateTimeField(verbose_name=_('дедлайн'))
	status = models.CharField(max_length=100, verbose_name=_('статус'))

	def __str__(self):
		return self.title