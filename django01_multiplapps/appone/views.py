from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def d1(request):

    list =[10,20,30,40,50]

    return HttpResponse(list)

