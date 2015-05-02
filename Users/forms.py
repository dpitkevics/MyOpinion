from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm

from Users.models import UserProfile


class UserCreationForm(BaseUserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        email = {
            'required': True,
        }


class AuthenticationForm(BaseAuthenticationForm):
    pass


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture']