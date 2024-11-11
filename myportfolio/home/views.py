from django.shortcuts import render,redirect
from . models import Project



# Create your views here.


def index(request):
   projects=Project.objects.all()
   return render(request,'index.html',{'projects':projects})


def detail_project(request,pk):
   project = Project.objects.get(pk=pk)
   images_by_project =project.images.all()
   videos=project.videos.all()
   return render(request,'detail_project.html',{'project':project,'images_by_project':images_by_project,'videos':videos})


