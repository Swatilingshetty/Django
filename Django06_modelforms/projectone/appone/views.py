from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

# def adduser(request):

#     form=forms.userprofileform()
#     if request.method == 'POST':
#         f=form.userprofileform(request.POST)
#         print(f)
    
#     return render(request,'adduser.html',{'form':form})

# cleaned data 
# def adduser(request):

#     form=forms.userprofileform()
#     if request.method =='POST':

#         f=form.userprofileform(request.POST)
#         if f.is_valid():
#             print(f.is_valid())
#             print(f.cleaned_data)
#             return HttpResponse("data submitted successfully")
        
#         else:
#             ff=forms.userprofileform()
#             print(ff.is_valid())
#             print(f.cleaned_data)
#             return HttpResponse("data not submitted")
            

#     return render(request,'adduser.html',{'form':form})

# for database we use this
def adduser(request):

    form=forms.userprofileform()
    if request.method =='POST':

        f=forms.userprofileform(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("data submitted successfulyy")
        else:

             return HttpResponse("data not submitted ")
        
    return render(request,'adduser.html',{'form':form})
