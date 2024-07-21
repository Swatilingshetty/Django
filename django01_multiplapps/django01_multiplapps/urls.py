
from django.contrib import admin
from django.urls import path
from appone import views  as l
from apptwo import views as t
from appthree import views as s


urlpatterns = [
    path('admin/', admin.site.urls),
    path('d1/',l.d1),
    path('d2/',t.d2),
    path('d3/',s.d3),
    
]
