from django.db import models
from django.contrib.auth.models import User

class ProgrammerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    language = models.CharField(max_length=30)
    frameworks = models.CharField(max_length=50)
    experience = models.PositiveIntegerField()


class Project(models.Model):
    programmer = models.ForeignKey(ProgrammerModel, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.CharField()

