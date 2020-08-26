from django.contrib import admin
from django.urls import path
from . views import create,detail,update,delete
#from .views import signup

urlpatterns = [
   path('create/', create, name='create'),
   path('detail/<int:student_id>', detail, name='detail'),
   path('update/<int:student_id>', update, name='update'),
   path('delete/<int:student_id>', delete, name='delete'),
]