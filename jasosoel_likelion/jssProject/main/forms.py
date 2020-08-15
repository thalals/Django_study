from django import forms
from .models import Jasoseol, Comment    #modelform을  쓰기위해서 forms import

#ModelForm 은 어떤 모델과 대응 되는 html Form을 생성하는것 
class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol        #대응되는 모델
        fields = ('title','content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class' : 'jss_title',      #class 태그? 를 지정해줌
            'placeholder' : '제목',
        })
    #   폼태그 이쁘게 -> class : form-control
    #  widgets = {
    #         'title': forms.TextInput(attrs={'id': 'title', 'class': 'form-control'}),
    #         'content': forms.Textarea(attrs={'id': 'content', 'class': 'form-control'}),
    #     }
    
class CommentForm(forms.ModelForm):

    class meta :
        model = Comment
        fields =('content',)