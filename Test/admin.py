from django.contrib import admin
from .models import *



@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display=['id','name','age','roll_no']


# Register your models here.
