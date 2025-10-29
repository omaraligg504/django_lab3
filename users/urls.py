from django.urls import path
from django.shortcuts import render
from .views import home

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

def logout_page(request):
    return render(request, 'logout.html')

urlpatterns = [
    path('', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_page, name='logout_page'),
    path('dashboard/', home, name='dashboard_page'),
]
