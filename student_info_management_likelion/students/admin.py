from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.StudentModel)
class studentsAdmin(admin.ModelAdmin):
    pass