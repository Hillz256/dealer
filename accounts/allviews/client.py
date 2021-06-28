from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth import login
from django.db.models import Count

from accounts.models import NewUser, Project, Proposal
from accounts.forms import ClientSignUpForm, ProposalForm


class ClientSignUpView(CreateView):
    model = NewUser
    form_class = ClientSignUpForm
    template_name = "accounts/registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Talent"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_client = True
        user.save()
        login(self.request, user)
        return redirect("client_dashboard")


class ClientDashboard(ListView):
    model = Project
    ordering = ("-date_added",)
    context_object_name = "projects"
    template_name = "accounts/client/client_dashboard.html"


class ProposalListView(ListView):
    model = Proposal
    context_object_name = "proposals"
    ordering = ("-date_added",)
    template_name = "accounts/client/proposals.html"
