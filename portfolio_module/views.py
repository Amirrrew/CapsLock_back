from django.contrib.admin import action
from django.shortcuts import render
from django.views.generic import DetailView, detail
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from portfolio_module.models import Project, SkillsCategory, Courses
from portfolio_module.serializers import ProjectSerializer, SkillCategorySerializer, CourseSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.prefetch_related('techs' ,'project_images').filter(is_active=True)
    serializer_class = ProjectSerializer

    @action(detail=False ,methods=['get'])
    def chosen(self ,request):
        projects = self.get_queryset().filter(chosen=True)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)

class SkillCategoryViewSet(ModelViewSet):
    queryset = SkillsCategory.objects.prefetch_related('skills_set').all()
    serializer_class = SkillCategorySerializer

class CoursesViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

    