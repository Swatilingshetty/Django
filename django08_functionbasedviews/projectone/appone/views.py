from django.shortcuts import render
from appone.models import product
from appone.forms import productform
from django.http import HttpResponseRedirect
# Create your views here.

def getproducts(request):

    products=product.objects.all()
    print(products)
    return render(request,'index.html',{'products':products})

def createproduct(request):

    form=productform()     # create an interface of the form
    if request.method == 'POST':      #if the from is submitted
        form=productform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect('/')
    return render(request,'create.html',{'form':form})

def updateproduct(request):
    product=product.objects.get(id=id)
    form=productform(instance=product)
    if request.method=='POST':
        form=productform(request.POST,instance=product)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'update.html',{'form':form})