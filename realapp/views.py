
from django.shortcuts import render


from django.views.generic import FormView
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth import *


# Create your views here.
class RegisterUserView(FormView):

        template_name = "realapp/register.html"
        form_class = RegisterUserForm
        success_url = '/thanks/'

        def form_valid(self, form):
            form.save()
            return HttpResponse("Registered")


class LoginUserView(FormView):

        template_name = "realapp/login.html"
        form_class = LoginUserForm

        def post(self, request, *args, **kwargs):
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(request,email=email,password=password)

                if user is not None:
                        login(request,user)
                else:
                        return HttpResponse("invalid")


class HomeUserView(FormView):
        pass


