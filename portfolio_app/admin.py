from django.contrib import admin

from .api.models.project import Project
from .api.models.language import Language
from .api.models.framework import Framework

admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Framework)
