from django.urls import path
from firstapp import views

urlpatterns=[
    path('products/',views.get_products),
]