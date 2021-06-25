from accounts.models import Project
from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

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
    fields = [
        "title",
        "text",
    ]


class ProjectUpdateView(UpdateView):
    model = Project
    fields = [
        "title",
        "text",
    ]


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = "/"
