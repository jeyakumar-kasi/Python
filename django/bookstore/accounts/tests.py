from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView


class CustomUserTest(TestCase):
    def test_create_user(self):
        userModel = get_user_model()
        user = userModel.objects.create_user(username='jkasi', email='dev.jeakumar@gmail.com', password='12345678')
        
        self.assertTrue(user.username, 'jkasi')
        self.assertTrue(user.email, 'dev.jeakumar@gmail.com')
        self.assertTrue(user.password, '12345678')
        self.assertTrue(user.is_active)
        
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
        
    def test_create_superuser(self):
        userModel = get_user_model()
        user = userModel.objects.create_superuser(username='jkasi', email='dev.jeakumar@gmail.com', password='12345678')
        
        self.assertTrue(user.username, 'jkasi')
        self.assertTrue(user.email, 'dev.jeakumar@gmail.com')
        self.assertTrue(user.password, '12345678')
        self.assertTrue(user.is_active)
        
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        
        
# Signup
class SignupPageTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
        
    def test_signup_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Signup')
        self.assertNotContains(self.response, 'Hi, I will not be exists in signup page')
                
    def test_signup_form_used(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
        
    def test_signup_view_used(self):
        resolved_view = resolve('/accounts/signup/') ## Should same as given in "urls.py" i.e => TRAILING '/' is MUST here!!! 
        self.assertEqual(resolved_view.func.__name__, SignupPageView.as_view().__name__)
        
        