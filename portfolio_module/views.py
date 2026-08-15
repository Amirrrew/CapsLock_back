from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from portfolio_module.models import Project
from portfolio_module.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.prefetch_related('techs' ,'project_images').all()
    serializer_class = ProjectSerializer

    