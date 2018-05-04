from  django import forms
from django.contrib.auth.models import User
from .models import *


class RegisterUserForm(forms.ModelForm):
        class Meta:
            model = User
            fields = '__all__'


class LoginUserForm(forms.Form):
        email = forms.EmailField(max_length=10)
        password = forms.CharField(widget=forms.PasswordInput)
