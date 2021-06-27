from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = "accounts/registration/signup.html"


class LoginView(TemplateView):
    template_name = "accounts/registration/login.html"
