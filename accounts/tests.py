from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Account

class LoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.account = Account(email='testuser@gmail.com')
        self.account.set_password('testpassword')
        self.account.is_active = True
        self.account.save()

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_success(self):
        response = self.client.post(reverse('login'), {'email': 'testuser@gmail.com', 'password': 'testpassword'})
        self.assertRedirects(response, '/')

    
    def test_bad_login(self):
        response = self.client.post(reverse('login'), {'email': 'test@gmail.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class RegisterViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        
    def test_register_success(self):
        response = self.client.post(reverse('register'), {'email': 'newuser@gmail.com', 'password1': 'aoifdjoasijfoias', 'password2': 'aoifdjoasijfoias'})
        self.assertEqual(response.status_code, 302)
    
    def test_bad_register(self):
        response = self.client.post(reverse('register'), {'email': '', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

class LogoutViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.account = Account(email='testuser@gmail.com')
        self.account.set_password('testpassword')
        self.account.is_active = True
        self.account.save()

    def test_logout_view(self):
        self.client.login(email='testuser@gmail.com', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/') 