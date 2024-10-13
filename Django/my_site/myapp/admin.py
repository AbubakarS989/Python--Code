from django.contrib import admin

#? give access of our new database to admin panel
from .models import ToDOList,Item
# Register your models here.
admin.site.register(ToDOList)
admin.site.register(Item)
