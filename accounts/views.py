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


class ProjectUpdateView(UpdateView):
    model = Project
    fields = [
        "title",
        "text",
    ]


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = "/"


class AddProposalView(CreateView):
    model = Proposal
    form_class = ProposalForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.project_id = self.kwargs["pk"]
        return super().form_valid(form)
