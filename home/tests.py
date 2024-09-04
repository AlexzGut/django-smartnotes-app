from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class HomeIndexViewTests(TestCase):
    def test_index_view_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

class HomeLoginInterfaceViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
    
    # test the -GET request-
    def test_login_interface_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/login.html')
    
    # test the -POST request-
    def test_login_interface_valid_data_post(self):
        user_login_data = {"username": "testuser", "password": "secret"}
        response = self.client.post(reverse('login'), user_login_data)
        self.assertEqual(response.status_code, 302)

    def test_login_interface_invalid_data_post(self):
        user_login_data = {"username": "invalidtestuser", "password": "secret"}
        response = self.client.post(reverse('login'), user_login_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

class HomeLogoutInterfaceViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
    
    def test_logout_interface(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/logout.html')

class HomeSignupViewTests(TestCase):
    # test the -GET- request
    def test_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/signup.html')

    def test_signup_valid_data_post(self):
        user_signup_data = {"username": "testuser", "password1": "Secret.123", "password2": "Secret.123"}
        response = self.client.post(reverse('signup'), user_signup_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())


    def test_signup_invalid_username_post(self):
        user_signup_data = {"username": "test'user", "password1": "Secret.123", "password2": "Secret.123"}
        response = self.client.post(reverse('signup'), user_signup_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter a valid username.')
        self.assertFalse(User.objects.filter(username="test'user").exists())

    def test_signup_invalid_password_post(self):
        user_signup_data = {"username": "testuser", "password1": "secret", "password2": "secret"}
        response = self.client.post(reverse('signup'), user_signup_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This password is too short. It must contain at least 8 characters')
        self.assertFalse(User.objects.filter(username="testuser").exists())

    def test_signup_passwords_do_not_match_post(self):
        user_signup_data = {"username": "testuser", "password1": "Secret.123", "password2": "Secret.1234"}
        response = self.client.post(reverse('signup'), user_signup_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The two password fields didn’t match.')
        self.assertFalse(User.objects.filter(username="testuser").exists())

