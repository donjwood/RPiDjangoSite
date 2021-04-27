from django.test import TestCase
from django.urls import reverse

"""
Test for views.
"""

class StaticPageViewTest(TestCase):

    def test_index_url(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_about_url(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_edit_user_url(self):
        response = self.client.get('/users/edit')
        self.assertEqual(response.status_code, 200)
    