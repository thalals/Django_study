from django.shortcuts import render,redirect, get_object_or_404
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404
# Create your views here.

def index(request) :
    all_jss = Jasoseol.objects.all()
    return render(request,"index.html",{ 'all_jss':all_jss})

def create(request) :
    if request.method =="POST" :
        filled_form = JssForm(request.POST)

        if filled_form.is_valid():          #데이터 유효성 검사
            filled_form.save()
            return redirect('index')
 
    jss_form = JssForm()
    return render(request,"create.html",{'jss_form' : jss_form})

def detail(request, jss_id) :
    # try : 
    #     my_jss = Jasoseol.objects.get(pk=jss_id)
    # except :
    #     raise Http404

    my_jss = get_object_or_404(Jasoseol, pk=jss_id)
    return render(request, "detail.html",{'my_jss':my_jss})

def delete(request, jss_id) :
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()     #object 제거

    return redirect('index')
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