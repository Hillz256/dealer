from django.db import reset_queries
from accounts.models import Project, Proposal
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from accounts.forms import ProjectForm, ProposalForm

# Create your views here.


def home(request):
    return render(request, "accounts/index.html")


class ProjectListView(ListView):
    model = Project
    ordering = "-date_added"
    context_object_name = "projects_list"
    template_name = "accounts/index.html"


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(UpdateView):
    model = Project
    fields = [
        "title",
        "text",
    ]


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = "/"
