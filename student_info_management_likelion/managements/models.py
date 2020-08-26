from django.db import models
from students import models as student_models
from django.contrib.auth.models import User
# Create your models here.

class UserModel(student_models.StudentModel):
    updated = models.DateTimeField(auto_now=True)
    