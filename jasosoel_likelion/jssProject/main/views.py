from django.shortcuts import render,redirect, get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request) :
    all_jss = Jasoseol.objects.all()
    return render(request,"index.html",{ 'all_jss':all_jss})

def my_index(request) :
    my_jss = Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html',{'all_jss' : my_jss})

# 모델.object.all()
# 모델.object.get()
# 모델.object.filter()
@login_required(login_url='/login/')    #login 필요하면 기능수행
def create(request) :
    # if request.user.is_authenticated:       #authenticated 인증이 안되어있으면
    #     return redirect('login')

    if request.method =="POST" :
        filled_form = JssForm(request.POST)

        if filled_form.is_valid():          #데이터 유효성 검사
            temp_form = filled_form.save(commit =False)     #Commit =False 는 잠시 저장되기전(업데이트 생성전) 저장 지연
            temp_form.author = request.user
            temp_form.save()    
            # filled_form.author = request.user
            # filled_form.save()
            return redirect('index')
 
    jss_form = JssForm()
    return render(request,"create.html",{'jss_form' : jss_form})

def detail(request, jss_id) :
    # try : 
    #     my_jss = Jasoseol.objects.get(pk=jss_id)
    # except :
    #     raise Http404

    my_jss = get_object_or_404(Jasoseol, pk=jss_id)
    comment_form = CommentForm()

    return render(request, "detail.html",{'my_jss':my_jss, 'comment_form':comment_form})

def delete(request, jss_id) :
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author:
        my_jss.delete()     #object 제거
        return redirect('index')

    raise PermissionDenied #위반 경고 메세지 출력
#모델폼 사용 업데이트
def update(request, jss_id) :
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance = my_jss)   #가져오고 싶은 object를 변수에 저장
    if request.method == "POST" :
        updated_form = JssForm(request.POST, instance=my_jss)   #instance 를 이용하여 객체에 덧쒸움
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')

    return render(request, 'create.html',{'jss_form':jss_form})

def create_comment(request, jss_id) :
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.sae(commit=False)
        temp_form.author =request.user
        temp_form.jasoseol = Jasoseol.object.get(pk=jss_id)
        temp_form.save()
    
        return redirect('detail', jss_id)


def delete_comment(request, jss_id, comment_id):
    my_comment = Comment.objects.get(pk=comment())
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail', jss_id)

    else :
        raise PermissionDenied
