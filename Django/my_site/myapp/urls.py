
from django.urls import path

#? import the view file from the current directory
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("<int:id>",views.lists,name="lists"),
    path("create/",views.create,name="create"),
    
    
    
]
