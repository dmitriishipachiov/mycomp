from django.shortcuts import render

from .models import *

def products(request):
    return render(request, 'goods/products.html')
