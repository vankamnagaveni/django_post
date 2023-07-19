from django.shortcuts import render
from django.http import HttpResponse

from .models import post

# Create your views here.

def index(request):
    
    veni = post.objects.all()
    
    print(veni)
    
    return render(request, 'index.html',context={'veni':veni})

def about(request):
    return render(request, 'about.html')
