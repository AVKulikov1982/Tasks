from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text=_('Имя'))
	last_name = forms.CharField(max_length=30, required=False, help_text=_('Фамилия'))
	email = forms.CharField(max_length=30, required=False, help_text=_('Мэйл'))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
	last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
	email = forms.CharField(max_length=30, required=False, help_text='email')
	new_pass1 = forms.CharField(max_length=30, required=False, widget=forms.PasswordInput, help_text='новый пароль')
	new_pass2 = forms.CharField(max_length=30, required=False, widget=forms.PasswordInput, help_text='новый пароль еще раз')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']


class UploadFileForm(forms.Form):
	file = forms.FileField(required=False)
