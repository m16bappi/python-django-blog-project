from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    def clean(self):
        clean_data = super(loginForm, self).clean()
        user = authenticate(username=clean_data['username'], password=clean_data['password'])

        if user is not None:
            pass
        else:
            raise ValidationError('username or password not correct')
