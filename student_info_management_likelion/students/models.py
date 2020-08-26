from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    major = models.CharField(max_length = 50)
    admission_year = models.CharField(max_length = 50)
    class_number = models.CharField(max_length=50)
    grade = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    