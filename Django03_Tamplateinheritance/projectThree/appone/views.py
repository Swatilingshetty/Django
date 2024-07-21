from django.shortcuts import render
# from django.template import loader

# Create your views here.
def about(request):
    
    return render(request,'about.html')

def contact(request):
    
    return render(request,'contact.html')

def home(request):
   

    return render(request,'home.html')

def services(request):
    
    return render(request,'services.html')

