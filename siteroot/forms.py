from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError

class EditUserForm(UserChangeForm):
    #first_name_char = forms.CharField(required=False)
    #last_name_char = forms.CharField(required=False)
    #email_char = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super(forms.RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
