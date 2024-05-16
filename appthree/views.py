from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def d3(request):

    # str=("sai kiran")

    return HttpResponse('<html style="color:red;"><h1>hii.. I am from three </h1></html>')