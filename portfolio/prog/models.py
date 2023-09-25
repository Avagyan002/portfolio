from django.db import models
from django.contrib.auth.models import User

class ProgrammerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    frameworks = models.CharField(max_length=50)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.user.get_full_name()

class Project(models.Model):
    programmer = models.ForeignKey(ProgrammerModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
