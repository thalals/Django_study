from django.db import models

# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    update_at = models.DateTimeField(auto_now = True)
    #날짜와 시간을 받음, auto_now = true 는 업데이트될때 날짜 자동저장

    # def __str__(self):
    #     return self.name