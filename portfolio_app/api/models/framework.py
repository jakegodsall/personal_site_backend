from django.db import models

from .language import Language


class Framework(models.Model):
    name = models.CharField(max_length=128, unique=True, blank=False)
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name="language")

    def __str__(self):
        return self.name
