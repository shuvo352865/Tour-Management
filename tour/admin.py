from django.contrib import admin
from .models import calculate
# Register your models here.


@admin.register(calculate)
class calculateModelAdmin(admin.ModelAdmin):
    list_display=['id','frm','destination','transport','hotel','person','day']