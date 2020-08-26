from django.shortcuts import render, redirect, get_object_or_404
from . models import student_models
from students.models import StudentModel
from signup.views import home
# Create your views here.
def create(request) :

    if request.method =="POST" :
        item = StudentModel()
        
        item.name = request.POST['name']
        item.major = request.POST['major']
        item.admission_year = request.POST['admission_year']
        item.class_number = request.POST['class_number']
        item.grade = request.POST['grade']
        item.user =request.user
        
        item.save()

        return redirect('home')
    
    return render(request,"create.html")

def update(request, student_id):
    item = get_object_or_404(StudentModel, pk=student_id)
    if request.method =='POST':
        item.name = request.POST['name']
        item.major = request.POST['major']
        item.admission_year = request.POST['admission_year']
        item.class_number = request.POST['class_number']
        item.grade = request.POST['grade']
        item.save()

        return redirect('detail', student_id)
    else:
        return render(request, 'update.html',{'items' : item})

def detail(request, student_id):
    item = get_object_or_404(StudentModel, pk=student_id)

    return render(request,'detail.html', {'item':item})

def delete(request, student_id):
    item=get_object_or_404(StudentModel, pk=student_id)
    item.delete()

    return redirect('home')
    