from django.shortcuts import render

from .models import *

def cart(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, 'cart/cart.html', context=context)
