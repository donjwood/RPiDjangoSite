from django.test import TestCase
from django.contrib.auth.models import User

"""
User model test.

Yes, probably unnecessary since it is built in, but using it to try
out Django's testing framework.
"""
class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='smokeywood', first_name='Smokey', last_name='Wood')
    
    def test_user_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_password_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_username_data(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'smokeywood')

    def test_firstname_data(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.first_name, 'Smokey')

    def test_lastname_data(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.last_name, 'Wood')
