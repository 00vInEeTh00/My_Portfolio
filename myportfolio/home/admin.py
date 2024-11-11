from django.contrib import admin
from .models import Project, ProjectImage, ProjectVideo, Category


# Register the models
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(ProjectVideo)
admin.site.register(Category)
