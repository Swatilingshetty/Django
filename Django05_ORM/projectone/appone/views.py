from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from appone.models import userprofile
from django.db.models import Avg,Sum,Min,Max,Count

# Create your views here.
def userprofiledetails(request):
    template=loader.get_template("userprofiledetails.html")
    details=userprofile.objects.all()
    d={"details":details}
    return HttpResponse(template.render(context=d))

# __contains
def containsusername(request):
    template=loader.get_template("containsusername.html")
    details=userprofile.objects.filter(username__contains="swati")
    d={"details":details}
    return HttpResponse(template.render(context=d))

# __icontains
def icontainsusername(request):
    template=loader.get_template("icontainsusername.html")
    details=userprofile.objects.filter(username__icontains="name")
    d={"details":details}
    return HttpResponse(template.render(context=d))

# __id__in
def id_in(request):
    template=loader.get_template("id_in.html")
    details=userprofile.objects.filter(id__in=[2,6,3])
    d={"details":details}
    return HttpResponse(template.render(context=d))

 #_startswith and istartswith
def startswith(request):
    template=loader.get_template("startswith.html")
    details=userprofile.objects.filter(username__istartswith="n")
    # details=userprofile.objects.filter(username__startswith="n")
    d={"details":details}
    return HttpResponse(template.render(context=d))


 #endswith
def endswith(request):
    template=loader.get_template("endswith.html")
    details=userprofile.objects.filter(username__endswith="n")
    d={"details":details}
    return HttpResponse(template.render(context=d))


#__exact
def idExact(request):
    template=loader.get_template("idExact.html")
    # details=userprofile.objects.filter(id__exact=None)
    # details=userprofile.objects.filter(id__exact=2)
    details=userprofile.objects.filter(username__exact="nameone")
    d={"details":details}
    return HttpResponse(template.render(context=d))

# or operator
def orOperator(request):
    template=loader.get_template("orOperator.html")
    details=userprofile.objects.filter(username__startswith="none")| userprofile.objects.filter(username__startswith="swati")
    d={"details":details}
    return HttpResponse(template.render(context=d))

# and 
def andOperator(request):
    template=loader.get_template("andOperator.html")
    # details=userprofile.objects.filter(username__startswith="bheem")& userprofile.objects.filter(username__startswith="bheem")
    details=userprofile.objects.filter(username__startswith="name")& userprofile.objects.filter(username__startswith="name")
    d={"details":details}
    return HttpResponse(template.render(context=d))

#  values
def valuesMethod(request):
    template=loader.get_template("userprofiledetails.html")
    details=userprofile.objects.all().values("username","email")
    d={"details":details}
    print(d)
    return HttpResponse(template.render(context=d))

# values_list()
def valuesListMethod(request):
    template=loader.get_template("userprofiledetails.html")
    details=userprofile.objects.all().values("username","email",named=True)
    d={"details":details}
    print(d)
    return HttpResponse(template.render(context=d))

# salary
def order_by(request):
    template=loader.get_template("order_by.html")
    details=userprofile.objects.all().order_by("salary")
    # details=userprofile.objects.all().order_by("-salary")
    # details=userprofile.objects.all().order_by("salary")[0:3]
    # details=userprofile.objects.all().order_by("username")[0:3]
    # details=userprofile.objects.all().order_by("username")
    # details=userprofile.objects.all().order_by("email")
    d={"details":details}
    return HttpResponse(template.render(context=d))

# avg
def avgsalary(request):
    template=loader.get_template("avgsalary.html")
    details=userprofile.objects.all().aggregate(Avg("salary"))
    print(details)
    d={"details":details}
    return HttpResponse(template.render(context=d))

# count
def count(request):
    template=loader.get_template("count.html")
    # details=userprofile.objects.all().aggregate(Count("salary"))
    details=userprofile.objects.all().aggregate(Count("username"))
    d={"details":details}
    print(d)
    return HttpResponse(template.render(context=d))

# MAX
def max(request):
    template=loader.get_template("max.html")
    details=userprofile.objects.all().aggregate(Max("salary"))
    # details=userprofile.objects.all().aggregate(Max("username"))
    d={"details":details}
    # print(d)
    return HttpResponse(template.render(context=d))

# Min
def min(request):
    template=loader.get_template("min.html")
    details=userprofile.objects.all().aggregate(Min("salary"))
    # details=userprofile.objects.all().aggregate(Min("username"))
    d={"details":details}
    print(d)
    return HttpResponse(template.render(context=d))


# sum
def sum(request):
    template=loader.get_template("sum.html")
    details=userprofile.objects.all().aggregate(Sum("salary"))
    # details=userprofile.objects.all().aggregate(sum("username"))
    d={"details":details}
    print(d)
    return HttpResponse(template.render(context=d))

# create()
def insertrecord(request):
    template=loader.get_template("insertrecord.html")
    details=userprofile.objects.create(username="harsha",email="harsha@gmail.com",contact=636445158,salary=35000)
    d={"details":details}
    return HttpResponse(template.render(context=d))

# save
def saverecord(request):
    template=loader.get_template("insertrecord.html")
    details=userprofile(username="harshith",email="harsha@gmail.com",contact=900872471,salary=30000)
    details.save()
    d={"details":details}
    return HttpResponse(template.render(context=d))


# bulk_create
def insertmultiplerecord(request):
    template=loader.get_template("insertrecord.html")
    details=userprofile.objects.bulk_create([
        userprofile(username="vishal",email="vishal@gmail.com",contact=900872471,salary=30000),
        userprofile(username="harshini",email="harshini@gmail.com",contact=900872471,salary=30000),
        userprofile(username="satya",email="satya@gmail.com",contact=900872471,salary=30000),
        userprofile(username="shashii",email="shashii@gmail.com",contact=900872471,salary=30000),
    ])
    d={"details":details}
    return HttpResponse(template.render(context=d))

# update()
def updaterecord(request):
    template=loader.get_template("insertrecord.html")
    details=userprofile.objects.get(id=8)
    details.salary=50000
    details.save()
    print(details.salary)
    d={"details":details}
    return HttpResponse(template.render(context=d))

# update()
# def updaterecord(request):
#    template=loader.get_template("insertrecord.html")
#    details=userprofile.objects.filter(username="bheem").update(salary="50000")
#    d={"details":details}
#    return HttpResponse(template.render(context=d))


# delete
# def deleterecord(request):
#     template=loader.get_template("insertrecord.html")
#     details=userprofile.objects.filter(username="bheem").delete()
#     d={"details":details}
#     return HttpResponse(template.render(context=d))

def deleterecord(request):
    template=loader.get_template("insertrecord.html")
    details=userprofile.objects.get(id=1)
    # details=userprofile.objects.all()
    details.delete()
    d={"details":details}
    return HttpResponse(template.render(context=d))

