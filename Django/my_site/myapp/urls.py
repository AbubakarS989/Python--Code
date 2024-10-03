
from django.urls import path

# import the view file from the current directory
from . import views

urlpatterns = [
    path("",views.index1,name="index1"),
    path("page1/",views.page1,name="page1"),
    
]
