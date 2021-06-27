from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse

# Create your models here.


class NewUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)


class Project(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})


class Proposal(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="proposals",
    )
    body = models.TextField()
    author = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.project.title, self.author)

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})


