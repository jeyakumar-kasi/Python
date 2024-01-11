from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


class TestHomePage(SimpleTestCase):
    
    def setUp(self):
        url = reverse("home_page") # Home page URL "name" in "pages/urls.py"
        self.response = self.client.get(url)
    
    def test_home_url_correct(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_home_page_template_is_used(self):
        self.assertTemplateUsed(self.response, "Home.html")
        
    def test_home_page_is_contains(self):
        # print(self.response.content)
        self.assertContains(self.response, "Books List")  # check inside of "<body>"
        
    def test_home_page_is_not_contains(self):
        self.assertNotContains(self.response, "Hi there!!!, It will not exists in homepage template")
        
    def test_home_page_template_is_correct(self):
        resolved_name = resolve("/").func.__name__
        self.assertEqual(resolved_name, HomePageView.as_view().__name__)
        
        
