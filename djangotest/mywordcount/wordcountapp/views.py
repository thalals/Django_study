from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request, 'home.html')

def test(request) :
    return render(request, 'test.html')

def test1(request) :
    return render(request, 'test1.html')

def test2(request) :
    return render(request, 'test2.html')