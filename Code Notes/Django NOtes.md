# Django NOtes


# This is environment for app not actual django app
-pip install django
-django-admin startproject my_site -> ["name of project"]
-cd  my_site [get into project first folder to run ]
-python manage.py runserver       [run-server on local machine]-> return url for our webpage

# This is for app
-python manage.py startapp myapp [code to create app after setup environment ]

# views file [in directory of app]
- it is type of platform where we write our html code  

# urls file

<!-- from django.urls import path

# import the view file from the current directory
from . import views

urlpatterns = [
    path("",views.index,name="index"),
] -->

# after this, now link the application [myapp] with project [my_site]

# migration 
-'myapp.apps.MyappConfig', 
-python manage.py migrate 
<!-- after crearing models  -->
python manage.py makemigrations myapp
-PS D:\Python-Code\Django\my_site> python manage.py shell


In [1]: from app.models import Item, ToDOList
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 from app.models import Item, ToDOList

ModuleNotFoundError: No module named 'app'

In [2]: from myapp.models import Item, ToDOList

In [3]: t=ToDOList(name="Bakar list")

In [4]: t.save()


In [6]: ToDOList.objects.all()
Out[6]: <QuerySet [<ToDOList: Bakar list>]>

In [7]: ToDOList.objects.get(id=1)
Out[7]: <ToDOList: Bakar list>

In [8]: ToDOList.objects.get(name="Bakar list")
Out[8]: <ToDOList: Bakar list>

In [10]: t.item_set.all()
Out[10]: <QuerySet []>


# data base query 
-t.filter(name__startswith="my")

<!-- to del an object -->
- In [31]: d=ToDOList.objects.get(id=2)

-In [32]: d.delete()

# Admin dashboard
- create login account
- python manage.py createsuperuser 

# give access to admin panel
-#? give access of our new database to admin panel
-from .models import ToDOList
-# Register your models here.
-admin.site.register(ToDOList)
