from django import forms
from .models import Jasoseol    #modelform을  쓰기위해서 forms import

#ModelForm 은 어떤 모델과 대응 되는 html Form을 생성하는것 
class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol        #대응되는 모델
        fields = ('title','content',)