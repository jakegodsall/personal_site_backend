from django.db import models

from .skill import Skill


class Project(models.Model):
    name = models.CharField(max_length=100)
    github_url = models.URLField()
    live_url = models.URLField()
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.name
