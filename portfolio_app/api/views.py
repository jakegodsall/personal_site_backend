from rest_framework import viewsets

from .models.project import Project
from .models.skill import Skill
from .serializers import ProjectSerializer, SkillSerializer

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
