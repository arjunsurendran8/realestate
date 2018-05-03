
from django.shortcuts import render

# from .forms import UserLoginForm
from django.views.generic import CreateView
from .forms import RegisterUserForm

# Create your views here.
class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "realapp/register.html"


