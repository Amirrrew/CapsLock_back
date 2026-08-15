from sys import maxsize

from django.db import models


class Tech(models.Model):
    title = models.CharField(max_length=200 ,verbose_name='Tech name')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural= 'Technologies'


class ProjectCategory(models.Model):
    title = models.CharField(max_length=100 ,null=False ,blank=False ,verbose_name='Project category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Project Categories'

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory ,null=False ,blank=False ,on_delete=models.CASCADE ,verbose_name='Project category')
    title = models.CharField(max_length=200 ,null=False ,blank=False ,verbose_name='Project title')
    desc = models.TextField(max_length=5000 ,null=True ,blank=True ,verbose_name='Description')
    production_date = models.DateField(null=True ,blank=True ,verbose_name='Production date')
    techs = models.ManyToManyField(Tech ,blank=False ,verbose_name='Technologies')
    url = models.CharField(max_length=500 ,null=True ,blank=True ,verbose_name='Project url')
    github_repos = models.CharField(max_length=500 ,null=True ,blank=True ,verbose_name='Github repository url')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=False ,null=True ,blank=True,verbose_name='Updated at')
    is_active = models.BooleanField(default=True ,verbose_name='Active / Inactive')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'My projects'


class ProjectImages(models.Model):
    img = models.ImageField(upload_to='projects' ,verbose_name='Image')
    project = models.ForeignKey(Project,on_delete=models.CASCADE ,null=True ,blank=True ,verbose_name='Project' ,related_name='project_images')
    is_main = models.BooleanField(default=False ,verbose_name='Is main image?')

    def __str__(self):
        return f'{self.project.title}-{self.pk}'

    class Meta:
        verbose_name_plural = 'Project images'




class SkillsCategory(models.Model):
    title = models.CharField(max_length=100 ,verbose_name='Skill category title')
    icon = models.CharField(max_length=1000 ,null=False ,blank=False ,verbose_name='Icon')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Skills categories'


class Skills(models.Model):
    category = models.ForeignKey(SkillsCategory ,on_delete=models.CASCADE ,null=False ,blank=False ,verbose_name='category')
    title = models.CharField(max_length=100 ,null=False ,blank=False ,verbose_name='Title')
    icon_svg = models.CharField(max_length=1000 ,null=True ,blank=True ,verbose_name='Icon')
    icon_img = models.ImageField(upload_to='skills' ,null=True ,blank=True ,verbose_name='Icon using image (in case there is no icon)')
    completion = models.IntegerField(default=0,null=True ,blank=True ,verbose_name='Completion percentage')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Skills carousel'



class Courses(models.Model):
    title = models.CharField(max_length=100 ,verbose_name='Title')
    start_date = models.CharField(max_length=100 ,null=True ,blank=True ,verbose_name='Start date')
    end_date = models.CharField(max_length=100 ,null=True ,blank=True ,verbose_name='End date')
    techs = models.ManyToManyField(Tech ,blank=False ,verbose_name='Techs learned')
