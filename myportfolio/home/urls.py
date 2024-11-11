from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'), 
    path('project_details/<pk>',views.detail_project, name='detail_project'),
       
    
]