from rest_framework import serializers

from portfolio_module.models import Project, Tech, ProjectCategory, ProjectImages, SkillsCategory, Skills, Courses


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = '__all__'

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = '__all__'

class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True ,read_only=True ,source='skills_set')
    class Meta:
        model = SkillsCategory
        fields = [
            'title',
            'icon',
            'skills'
        ]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    techs = TechSerializer(many=True, read_only=True)
    category = ProjectCategorySerializer(many=False ,read_only=True)
    project_images = ProjectImagesSerializer(many=True ,read_only=True)
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'title_fa',
            'techs',
            'category',
            'project_images',
            'desc',
            'url',
            'is_dev',
            'github_repos',
            'production_date',
            'updated_at',
        ]