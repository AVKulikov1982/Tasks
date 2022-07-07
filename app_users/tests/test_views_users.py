from django.test import TestCase
from django.urls import reverse
from ..models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login


class UsersViewsTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		user = User.objects.create(
			username='test_user',
			email='test@test.ru',
			password='qwepoijhgvcxz'
		)
		Profile.objects.create(user=user)

	def test_login(self):
		url = reverse('login')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'login.html')

	def test_logout(self):
		url = reverse('logout')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 302)

	def test_profile(self):
		url = reverse('profile', args=[1])
		self.client.login(username='test_user', password='qwepoijhgvcxz')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'profile.html')

	def test_profile_update_first_name(self):
		url = reverse('profile_update', args=[5])
		user = User.objects.get(id=5)
		self.client.login(username='test_user', password='qwepoijhgvcxz')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'profile_update.html')
		response = self.client.post(url, {
			'username': 'test_newusername',
			'first_name': 'test_first_name',
			'last_name': 'test_last_name',
			'email': 'test@test.ru',
			'new_pass1': '941$qwsadfeqwergbgb',
			'new_pass2': '941$qwsadfeqwergbgb'
		})
		user.refresh_from_db()
		self.assertEqual(response.status_code, 302)
		self.assertEqual(user.username, 'test_newusername')
		self.assertEqual(user.first_name, 'test_first_name')
		self.assertEqual(user.last_name, 'test_last_name')
		self.assertEqual(user.email, 'test@test.ru')
		self.assertTrue(self.client.login(username='test_newusername', password='941$qwsadfeqwergbgb'))

	def test_can_register(self):
		url = reverse('registration')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration.html')

		response = self.client.post(url, {
			'username': 'test_username',
			'password1': 'poijhgvcxz',
			'password2': 'poijhgvcxz'
		})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Profile.objects.last().user.username, 'test_username')
