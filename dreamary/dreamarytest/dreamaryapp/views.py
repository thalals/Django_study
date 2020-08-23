from django.shortcuts import render, redirect, get_object_or_404
from .models import Designer

# Create your views here.

def home(request) :
    designers = Designer.objects.all()
    return render(request, 'home.html',{'designers' : designers})

def introduce(request) :
    return render(request, 'introduce.html')

#designer_id 는 pk 이름
def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk = designer_id)
    return render(request, 'detail.html', {'designer' : designer})

def new(request) :
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        post = Designer()

        #파일이 있는지 체크
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()

        #import redirect 해줘야함 -> 페이지 돌리기
        return redirect('detail', post.id)

def update(request) :
    post = get_object_or_404(Designer, pk = designer_id)

    if request.method == 'POST':
        #파일이 있는지 체크
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()
        return redirect('detail', post.id)

    else :  #전송 방식이 get일 경우 기존의 정보 'post'를 뛰어줌
        return render(request,'update.html',{'designer' : post})

def delete(request, designer_id):
    post = get_object_or_404(Designer, pk = designer_id)
    post.delete()

    return redirect('home')


