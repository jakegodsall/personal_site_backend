from django.db import models


class Framework(models.Model):
    name = models.CharField(max_length=128, unique=True, blank=False)

    def __str__(self):
        return self.name
