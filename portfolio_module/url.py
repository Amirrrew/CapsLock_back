from rest_framework.routers import DefaultRouter
from portfolio_module.views import ProjectViewSet

router = DefaultRouter()
router.register('projects' ,ProjectViewSet)

urlpatterns = router.urls