
from django.contrib import admin
from django.urls import path
from appone import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.welcomeMessage),
    path('dictitems/',views.dictitems),
    path('filters/',views.filters),
    path('getproducts/',views.getproducts),
    path('getID/',views.getID),
]
