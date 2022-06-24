from django.test import TestCase
from django.urls import reverse

class MainViewsTest(TestCase):

	def test_index(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	def test_contacts(self):
		url = reverse('contacts')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'contacts.html')
