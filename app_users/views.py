from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import generic, View
from django.utils.translation import gettext_lazy as _
from .models import Profile, Avatar
from .forms import RegisterForm, UpdateProfileForm, UploadFileForm, ProfileRegisterForm
from app_main.views import logger


class UserLoginView(LoginView):
	"""Представление страницы входа пользователя"""
	template_name = 'login.html'
	logger.info('Аутентификация пользователя')


class UserLogoutView(LogoutView):
	"""Представление страницы выхода пользователя"""
	template_name = 'logout.html'


class UpdateProfileView(View):
	"""Представление страницы обновления профиля пользователя"""
	@staticmethod
	def get(request, user_id):
		avatar = None
		user = User.objects.get(id=user_id)
		user_form = UpdateProfileForm(instance=user)
		avatar_form = UploadFileForm()
		if Profile.objects.filter(user_id=user_id):
			profile_update = Profile.objects.get(user_id=user_id)
			update_form = UpdateProfileForm(instance=profile_update)
		else:
			update_form = UpdateProfileForm(instance=user)
		if Avatar.objects.filter(user_id=user_id):
			avatar = Avatar.objects.get(user_id=user_id).file

		return render(request, 'profile_update.html',
					  context={'user_form': user_form, 'avatar': avatar, 'update_form': update_form,
							   'avatar_form': avatar_form})

	@staticmethod
	def post(request, user_id):
		user = User.objects.get(id=user_id)
		avatar_form = UploadFileForm(request.POST, request.FILES)
		if Profile.objects.filter(user_id=user_id):
			profile_update = Profile.objects.get(user_id=user_id)
			update_form = UpdateProfileForm(request.POST, instance=profile_update)
		else:
			update_form = UpdateProfileForm(instance=user)

		if update_form.is_valid():
			user.username = update_form.cleaned_data.get('username')
			user.first_name = update_form.cleaned_data.get('first_name')
			user.last_name = update_form.cleaned_data.get('last_name')
			user.email = update_form.cleaned_data.get('email')
			user.save()
			values_for_update = {'user': user}
			Profile.objects.update_or_create(user_id=user_id, defaults=values_for_update)
			if update_form.cleaned_data.get('new_pass1') \
					and update_form.cleaned_data.get('new_pass1') == update_form.cleaned_data.get('new_pass2'):
				user.set_password(update_form.cleaned_data.get('new_pass1'))
				user.save()

		if avatar_form.is_valid():
			file = avatar_form.cleaned_data.get('file')
			if file:
				file_name = user.username + '.' + file.name.split('.')[-1]
				file.name = file_name
				values_for_update = {'user': user, 'file': file}
				Avatar.objects.update_or_create(user_id=user_id, defaults=values_for_update)

		return redirect('/')


def register(request):
	"""Представление страницы регистрации пользователя"""
	if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		profile_register_form = ProfileRegisterForm(request.POST)
		if register_form.is_valid():
			user = register_form.save()
			if profile_register_form.is_valid():
				department = profile_register_form.cleaned_data.get('department')
				Profile.objects.create(user=user, department=department)
			username = register_form.cleaned_data.get('username')
			row_password = register_form.cleaned_data.get('password1')

			user = authenticate(username=username, password=row_password)
			logger.info(f'Аутентификация пользователя {username}')
			login(request, user)
			return render(request, 'main.html')
	else:
		register_form = RegisterForm()
		profile_register_form = ProfileRegisterForm()
	return render(request, 'registration.html', context={'register_form': register_form, 'profile_register_form': profile_register_form})


def profile(request, user_id):
	"""Представление страницы профиля пользователя"""
	avatar = None
	if request.user.is_superuser:
		Profile.objects.get_or_create(user_id=user_id)
	if Avatar.objects.filter(user_id=user_id):
		avatar = Avatar.objects.get(user_id=user_id).file
	return render(request, 'profile.html', context={'avatar': avatar})
