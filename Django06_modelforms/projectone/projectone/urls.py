
from django.contrib import admin
from django.urls import path
from appone import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adduser/',views.adduser),
    
]
