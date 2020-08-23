from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    regi_form = UserCreationForm()      #장고에서 제공하는 회원가입 모델폼
    if request.method =="POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')

    return render(request,'signup.html',{'regi_form' : regi_form})