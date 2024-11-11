from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=40)
    short_description = models.CharField(max_length=120)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    priority=models.IntegerField(default=0)
    hide = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE ,null=True)
    image = models.ImageField(upload_to='images/',null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class ProjectVideo(models.Model):
    project = models.ForeignKey(Project, related_name="videos", on_delete=models.CASCADE,null=True)
    video_url = models.URLField(max_length=990,null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    iframe_url = models.CharField("Iframe URL", max_length=1000,null=True,blank=True)
    def __str__(self):
        return f"Video for {self.project.title}"
