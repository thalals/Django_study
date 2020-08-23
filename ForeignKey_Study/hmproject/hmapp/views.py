from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.
def home(request) :
    
    return render (request,'home.html')

def signup(request) :

    return render(request,'signup.html')

