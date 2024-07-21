from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from appone.models import userprofile

# Create your views here.
def userprofiledetails(request):
    template=loader.get_template("userprofiledetails.html")
    details=userprofile.objects.all()
    d={"informations":details}
    return HttpResponse(template.render(context=d))

# __contains
def containsusername(request):
    template=loader.get_template("containsusername.html")
    details=userprofile.objects.filter(username__contains="d")
    d={"informations":details}
    return HttpResponse(template.render(context=d))
