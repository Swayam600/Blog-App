from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from Blog.views import *

def user_register(request):
    return render(request, 'user-register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
            
        else:
            return redirect('login.html')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'home.html')