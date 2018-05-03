from  django import  forms
from django.contrib.auth.models import User
from .models import Registration

class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = '__all__'
