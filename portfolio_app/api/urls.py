from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, SkillViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('skill', SkillViewSet, basename='skill')

urlpatterns = router.urls
