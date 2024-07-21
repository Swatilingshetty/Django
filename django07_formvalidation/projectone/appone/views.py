from django.shortcuts import render
from . import forms

# Create your views here.
# def userprofileview(request):

#     form=forms.userprofileform()
#     return render(request,'userprofile.html',{'form':form})

# def userprofileview(request):

#     form=forms.userprofileform()
#     if request.method=='POST':
#         form=forms.userprofileform(request.POST)
#         if form.is_valid():
#            print("validation success:")
#            print("first name:", form.cleaned_data['first_name'])
#            print("last name:", form.cleaned_data['last_name'])
#            print("emails:", form.cleaned_data['email'])
#            print("phone:", form.cleaned_data['phone'])

#     return render(request,'userprofile.html',{'form':form})

def userprofileview(request):

    form=forms.userprofileform()
    if request.method=='POST':
        form=forms.userprofileform(request.POST)
        if form.is_valid():
           print(form.cleaned_data)
           

    return render(request,'userprofile.html',{'form':form})