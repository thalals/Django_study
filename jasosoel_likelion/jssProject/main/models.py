from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    update_at = models.DateTimeField(auto_now = True)
    #날짜와 시간을 받음, auto_now = true 는 업데이트될때 날짜 자동저장
    #on_delete -> 연결된 object가 지워졌을때
    author = models.ForeignKey(User, on_delete=models.CASCADE) #빈칸을 허용해주거나, defualt 값 지정