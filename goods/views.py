from django.shortcuts import render

from .models import *

def products(request):
    context = {
        'title': 'Товары'
    }
    return render(request, 'goods/products/products.html', context=context)

def womens(request):
    return render(request, 'goods/products/womens.html')
