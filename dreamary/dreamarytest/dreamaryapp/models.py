from django.db import models

# Create your models here.
class Designer(models.Model) :  #models.Model 은 고정(형식)
    image = models.ImageField(upload_to ='images/') #미디어에 있는 images에 올릴거다
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    description = models.TextField()
