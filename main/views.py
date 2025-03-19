from django.shortcuts import render

from .models import *

def index(request):
    context = {
        'title': 'Магазин'
    }
    return render(request, 'main/index.html', context=context)


def blog(request):
    context = {
        'title': 'Блог'
    }
    return render(request, 'main/blog/blog.html', context=context)


def post(request):
    context = {
        'title': 'Пост'
    }
    return render(request, 'main/blog/post.html', context=context)
