from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea
from accounts.models import Proposal, Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            "title",
            "text",
        )

        widgets = {"title": TextInput(), "text": Textarea()}


class ProposalForm(ModelForm):
    class Meta:
        model = Proposal
        fields = (
            "author",
            "body",
        )

        widgets = {"author": TextInput(), "body": Textarea()}
