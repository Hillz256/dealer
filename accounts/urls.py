from django.urls import path

from accounts.views import (
    ProjectCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
    AddProposalView,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="projects"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("projects/create/", ProjectCreateView.as_view(), name="create-project"),
    path("project/<int:pk>/update", ProjectUpdateView.as_view(), name="project_update"),
    path("project/<int:pk>/delete", ProjectDeleteView.as_view(), name="project_delete"),
    path(
        "project/<int:pk>/proposal", AddProposalView.as_view(), name="create_proposal"
    ),
]
