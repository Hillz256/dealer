from django.db import models
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea
from accounts.models import NewUser, Proposal, Project
from django.contrib.auth.forms import UserCreationForm


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


class ClientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = NewUser

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_client = True
            user.save()
            return user


class ProviderSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = NewUser
