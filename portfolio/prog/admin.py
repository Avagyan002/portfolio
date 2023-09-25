from django.contrib import admin
from .models import ProgrammerModel, Project

admin.site.register(ProgrammerModel)
admin.site.register(Project)
