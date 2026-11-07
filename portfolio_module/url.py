from rest_framework.routers import DefaultRouter
from portfolio_module.views import ProjectViewSet, SkillCategoryViewSet, CoursesViewSet

router = DefaultRouter()
router.register('projects' ,ProjectViewSet ,basename='projects')
router.register('skills' ,SkillCategoryViewSet)
router.register('courses' ,CoursesViewSet)

urlpatterns = router.urls