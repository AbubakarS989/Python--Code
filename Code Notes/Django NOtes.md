# Django NOtes


# This is environment for app not actual django app
-pip install django
-django-admin startproject [my_site, "name of project"]
-cd  my_site [get into project folder to run ]
-python manage.py runserver       [run-server on local machine]

# This is for app
-python manage.py startapp myapp [code to create app after setup environment ]

# views [in directory of app]
- it is type of platform where we write our html code  

# urls file

<!-- from django.urls import path

# import the view file from the current directory
from . import views

urlpatterns = [
    path("",views.index,name="index"),
] -->

# after this, now link the application [myapp] with project [my_site]