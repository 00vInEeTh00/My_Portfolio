from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'), 
    #path('', views.portfolio_create, name='portfolio_create'),   # URL for homepage
    path('home',views.home,name='home')
    
]