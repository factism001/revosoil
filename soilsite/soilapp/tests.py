from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class YourAppViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='testemail@gmail.com')
        self.login_url = reverse('login')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_successful_login(self):
        login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(self.login_url, data=login_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful login


    def test_user_dashboard_view(self):
        self.client.login(username='testuser', password='testpassword')  # Login the user
        response = self.client.get(reverse('user_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_dashboard.html')

    def test_soil_properties_analysis_view(self):
        self.client.login(username='testuser', password='testpassword')  # Login the user
        response = self.client.get(reverse('soil_properties_analysis'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'soil_properties_input_form.html')

        # Test a POST request to this view
        response = self.client.post(reverse('soil_properties_analysis'), data={})
        self.assertEqual(response.status_code, 200)  # If form is not valid, it should return the same page.

    def test_chat_view(self):
        self.client.login(username='testuser', password='testpassword')  # Login the user
        response = self.client.get(reverse('chat_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat_page.html')

        # Test a POST request to this view
        response = self.client.post(reverse('chat_view'), data={'prompt': 'Hello'})
        self.assertEqual(response.status_code, 200)  # If the model response is not implemented, it should return the same page.


