from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from accounts.models import NewUser, Project
from accounts.forms import ProviderSignUpForm


class ProviderSignUpView(CreateView):
    model = NewUser
    form_class = ProviderSignUpForm
    template_name = "accounts/registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Work"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_provider = True
        user.save()
        login(self.request, user)
        return redirect("provider_dashboard")


class ProviderDashboard(ListView):
    model = Project
    context_object_name = "projects_list"
    ordering = ("-date_added",)
    template_name = "accounts/provider/pro_dashboard.html"
