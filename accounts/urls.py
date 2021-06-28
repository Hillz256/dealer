from django.urls import path, include

from accounts.views import (
    ProjectCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
    home,
)

from accounts.allviews import client, provider

urlpatterns = [
    # path("", home, name="home"),
    path("", ProjectListView.as_view(), name="projects"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("projects/create/", ProjectCreateView.as_view(), name="create-project"),
    path("project/<int:pk>/update", ProjectUpdateView.as_view(), name="project_update"),
    path("project/<int:pk>/delete", ProjectDeleteView.as_view(), name="project_delete"),
    path(
        "project/<int:pk>/proposal",
        provider.ProposalCreateView.as_view(),
        name="create_proposal",
    ),
    path(
        "accounts/dashboard/client/",
        client.ClientDashboard.as_view(),
        name="client_dashboard",
    ),
    path(
        "accounts/dashboard/provider/",
        provider.ProviderDashboard.as_view(),
        name="provider_dashboard",
    ),
    path(
        "accounts/dashboard/client/proposals",
        client.ProposalListView.as_view(),
        name="proposals",
    ),
]
