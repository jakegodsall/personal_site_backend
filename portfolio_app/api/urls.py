from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, LanguageViewSet, FrameworkViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('language', LanguageViewSet, basename='language')
router.register('framework', FrameworkViewSet, basename='framework')

urlpatterns = router.urls
