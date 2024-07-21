"""
URL configuration for projectone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',views.productlistview.as_view()),
    path('<int:pk>/',views.productDetailview.as_view()),        #pk-primary key
    path('products/create/',views.productCreateview.as_view()),
    path('product/update/<int:pk>/',views.productUpdateview.as_view()),
    path('product/delete/<int:pk>/',views.productDeleteview.as_view()),
]