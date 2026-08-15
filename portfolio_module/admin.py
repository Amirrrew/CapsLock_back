from django.contrib import admin

from portfolio_module.models import Project, ProjectImages, Tech, SkillsCategory, Skills, ProjectCategory, Courses


class ProjectImageAdmin(admin.TabularInline):
    model = ProjectImages
    extra = 1

class SkillAdmin(admin.TabularInline):
    model = Skills
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_filter = ['created_at' ,]
    list_display = ['title' ,'created_at' ,'is_active']
    list_editable = ['is_active']
    inlines = [ProjectImageAdmin]

class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    inlines = [SkillAdmin]


admin.site.register(ProjectCategory)
admin.site.register(Project ,ProjectAdmin)
admin.site.register(Tech)
admin.site.register(SkillsCategory ,SkillCategoryAdmin)
admin.site.register(Courses)
