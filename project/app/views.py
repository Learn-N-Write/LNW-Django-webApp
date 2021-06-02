from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse


# Create your views here.

def home(request):
    return  render(request,"index.html")

def contact(request):
    return  render(request,"contact.html")
