from django.db import models

from .skill import Skill


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True, blank=False)
    github_url = models.URLField(blank=True)
    live_site_url = models.URLField(blank=True)
    # screenshot = models.ImageField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    skills = models.ManyToManyField(Skill, related_name="skill")

    def __str__(self):
        return self.name
