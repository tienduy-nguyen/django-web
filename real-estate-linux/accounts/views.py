from django.shortcuts import render, redirect
from django.http import HttpRequest

# Create your views here.


def login(request):
    return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
      # Register User
        print('SUBMITTED REG')
        return redirect('register')
    else:
        return render(request, 'auth/register.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'auth/dashboard.html')
