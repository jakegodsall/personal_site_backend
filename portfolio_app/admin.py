from django.contrib import admin

from .api.models.project import Project
from .api.models.skill import Skill

admin.site.register(Project)
admin.site.register(Skill)
