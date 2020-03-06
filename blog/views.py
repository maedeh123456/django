from django.shortcuts import render
from blog.models import Blog

# Create your views here.

def list(request):
    pblog = Blog.objects.all()
    return render(request,'list.html',{'posts':pblog})

def details(request):
    posts = Blog.objects.all()
    return render(request,'details.html',{'posts':posts})