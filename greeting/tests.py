from django.test import TestCase, Client
from django.urls import reverse
from greeting.views import format_greeting

class GreetingTests(TestCase):
    def setUp(self):
        """Set up test client"""
        self.client = Client()
    
    def test_format_greeting(self):
        """Test the greeting formatter function"""
        result = format_greeting("John")
        self.assertEqual(result, "Hello, John! Welcome to our application.")
    
    def test_index_page(self):
        """Test that index page loads correctly"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Django Greeting App")
        self.assertContains(response, '<form action')
    
    def test_greet_post_with_name(self):
        """Test greeting with a name"""
        response = self.client.post(reverse('greet'), {'name': 'TestUser'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestUser")
        self.assertContains(response, "Hello, TestUser! Welcome to our application.")
    
    def test_greet_post_empty_name(self):
        """Test greeting with empty name - should use default 'Guest'"""
        response = self.client.post(reverse('greet'), {'name': 'Guest'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Guest")
        self.assertContains(response, "Hello, Guest! Welcome to our application.")
    
    def test_greet_get_request(self):
        """Test that GET request to greet redirects to form"""
        response = self.client.get(reverse('greet'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Django Greeting App")