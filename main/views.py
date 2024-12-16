from django.shortcuts import render

from .models import *

def index(request):
    return render(request, 'main/index.html')


def blog(request):
    return render(request, 'blog/blog.html')
