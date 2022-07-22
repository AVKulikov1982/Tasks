from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Department(models.Model):
	"""Модель Отдел"""
	name = models.CharField(max_length=20, verbose_name=_('отдел'))

	def __str__(self):
		return self.name


class Profile(models.Model):
	"""Модель Профиль пользователя"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.IntegerField(null=True, verbose_name=_('номер телефона'))
	date_of_birth = models.DateTimeField(null=True, verbose_name=_('дата рождения'))
	department = models.ForeignKey(Department, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username


class Avatar(models.Model):
	"""Модель Аватар пользователя"""
	file = models.ImageField(null=True, blank=True, upload_to='avatars/')
	user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		super(Avatar, self).save(*args, **kwargs)
		print(self.file)
		if self.file:
			filename = self.file.path
			width = self.file.width
			height = self.file.height
			max_size = max(width, height)
			image = Image.open(filename)

			if max_size > 45:
				image = image.resize((45, 45), Image.ANTIALIAS)

			image.save(filename)
