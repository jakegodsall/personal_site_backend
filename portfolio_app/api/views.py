from rest_framework import viewsets

from .models.project import Project
from .models.language import Language
from .models.framework import Framework
from .serializers import ProjectSerializer, LanguageSerializer, FrameworkSerializer

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class FrameworkViewSet(viewsets.ModelViewSet):
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer
