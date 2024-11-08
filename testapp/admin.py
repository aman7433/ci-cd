from django.contrib import admin
from .models import modeldata
# Register your models here.
@admin.register(modeldata)

class admindata(admin.ModelAdmin):
    list_display=['id','name','password','email']