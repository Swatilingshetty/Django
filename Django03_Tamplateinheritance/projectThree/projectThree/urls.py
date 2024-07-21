
from django.contrib import admin
from django.urls import path
from appone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('services/',views.services),
]
