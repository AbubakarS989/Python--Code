from django.shortcuts import render

# import http for links
from django.http import HttpResponse

# Create your views here.
# ? Each function represent each view
def index1(response): 
    return  HttpResponse("Helo world from django!")

def page1(response): 
    return  HttpResponse("From page 1")
