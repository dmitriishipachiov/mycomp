from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth


from users.forms import UserLoginForm

def login(request):
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context=context)
