from django.contrib import admin
from accounts.models import NewUser, Project, Proposal

# Register your models here.

admin.site.register(NewUser)
admin.site.register(Project)
admin.site.register(Proposal)
