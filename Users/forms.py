from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm

from Users.models import UserProfile


class UserCreationForm(BaseUserCreationForm):
    pass


class UserChangeForm(BaseUserChangeForm):
    pass


class AuthenticationForm(BaseAuthenticationForm):
    pass


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rating']