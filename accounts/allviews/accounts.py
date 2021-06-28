from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from django.contrib import messages

from django.contrib.auth import login, authenticate, logout


class SignUpView(TemplateView):
    template_name = "accounts/registration/signup.html"


class LoginView(TemplateView):
    template_name = "accounts/registration/login.html"


def UserLoginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_client:
                return redirect("client_dashboard")
            else:
                return redirect("provider_dashboard")

        else:
            messages.info(request, f"Username or password is not correct")
    context = {}
    return render(request, "accounts/registration/login_form.html", context)


def LogoutView(request):
    logout(request)
    return redirect("projects")
