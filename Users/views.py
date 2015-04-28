from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from Users import forms


class RegisterView(View):
    template_name = 'Users/register.html'

    def get(self, request):
        user_form = forms.UserCreationForm()
        user_profile_form = forms.UserProfileForm()

        context = {
            'user_form': user_form,
            'user_profile_form': user_profile_form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        user_form = forms.UserCreationForm(request.POST)
        user_profile_form = forms.UserProfileForm(request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()

            messages.add_message(request, messages.SUCCESS, _('User successfully registered. You may now login.'))

            return HttpResponseRedirect(reverse('Users:register_success'))

        context = {
            'user_form': user_form,
            'user_profile_form': user_profile_form,
        }

        return render(request, self.template_name, context)


class LoginView(View):
    template_name = 'Users/login.html'

    def get(self, request):
        authentication_form = forms.AuthenticationForm()

        context = {
            'authentication_form': authentication_form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        authentication_form = forms.AuthenticationForm(None, request.POST)

        if authentication_form.is_valid():
            user = authenticate(username=authentication_form.cleaned_data['username'],
                                password=authentication_form.cleaned_data['password'])

            if user:
                if user.is_active:
                    login(request, user)

                    messages.add_message(request, messages.SUCCESS, _('You have been successfully logged in'))

                    return HttpResponseRedirect(reverse('Topics:index'))
                else:
                    messages.add_message(request, messages.ERROR, _('Your account is disabled'))
            else:
                messages.add_message(request, messages.ERROR, _('Invalid login details supplied'))

        context = {
            'authentication_form': authentication_form,
        }

        return render(request, self.template_name, context)


@login_required
def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('Topics:index'))