from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')

urlpatterns = router.urls
