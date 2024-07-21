from django.contrib import admin
from appone.models import userprofile
# Register your models here.

class userprofileadmin(admin.ModelAdmin):
    list_display=("username","email","contact")
    search_fields=("username",)
admin.site.register(userprofile,userprofileadmin)
