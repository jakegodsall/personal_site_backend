from django.db import models

from .language import Language
from .framework import Framework


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True, blank=False)
    github_url = models.URLField(blank=True)
    live_site_url = models.URLField(blank=True)
    # screenshot = models.ImageField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    languages = models.ManyToManyField(Language, related_name="language")
    frameworks = models.ManyToManyField(Framework, related_name="framework")

    def __str__(self):
        return self.name
