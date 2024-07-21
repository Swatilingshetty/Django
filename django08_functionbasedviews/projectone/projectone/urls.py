
from django.contrib import admin
from django.urls import path
from appone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.getproducts),
    path('product/create/',views.createproduct),
    path('product/create/<int:id>',views.updateproduct),
]
