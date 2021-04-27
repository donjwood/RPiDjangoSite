from django.test import TestCase
from siteroot.forms import EditUserForm
from django.contrib.auth.models import User

"""
Edit User Form Test
"""

class EditUserFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='smokeywood', first_name='Smokey', last_name='Wood')

    def test_edit_user_form_username_label(self):
        form = EditUserForm()
        self.assertEqual(form.fields['username'].label, 'Username')

    def test_edit_user_form_first_name_label(self):
        form = EditUserForm()
        self.assertEqual(form.fields['first_name'].label, 'First name')

    def test_edit_user_form_last_name_label(self):
        form = EditUserForm()
        self.assertEqual(form.fields['last_name'].label, 'Last name')

    def test_edit_user_form_email_label(self):
        form = EditUserForm()
        self.assertEqual(form.fields['email'].label, 'Email address')

    def test_edit_user_form_first_name_label(self):
        form = EditUserForm()
        self.assertEqual(form.fields['first_name'].label, 'First name')

    def test_edit_user_form_email_valid(self):
        form = EditUserForm()
        form = EditUserForm(data={'username': 'ninawood','email': 'foobar'})
        self.assertFalse(form.is_valid())
        form = EditUserForm(data={'email': 'foobar@nowhere'})
        form.data['email'] = 'foobar@nowhere'
        self.assertFalse(form.is_valid())
        form.data['email'] = 'foobar@nowhere.com'
        self.assertTrue(form.is_valid())
        