from django.shortcuts import render

# import http for links
from django.http import HttpResponse,HttpResponseRedirect

# access data from database
from .models import ToDOList,Item
# import forms
from .forms import CreateNewList
# Create your views here.
# ? Each function represent each view

    
def home(response):
    return render(response,"myapp/home.html",{})

def lists(response,id):
    lis=ToDOList.objects.get(id=id)
    return render(response,"myapp/lists.html",{"list":lis})

def create(response) :
    if response.method=="POST":
        form=CreateNewList(response.POST)
        
        if form.is_valid():
            n=form.cleaned_data["name"]
            t=ToDOList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
            
        
    else:
        form=CreateNewList()
    return render(response,"myapp/create.html",{"form":form})
 