from django.shortcuts import render
from django.template import loader
from django .http import HttpResponse

# VARIABLES
def welcomeMessage(request):

    template=loader.get_template('welcomeMessage.html')
    text={'welcome':'welcome to django template language'}
    return HttpResponse(template.render(context=text))

# VARIABLES
def dictitems(request):

    template=loader.get_template('dictitems.html')
    text={'nameone':'sai kiran','nametwo':'sai kumar','namethree':'sai ram'}
    return HttpResponse(template.render(context=text))

# filters
def filters(request):
    template=loader.get_template('filters.html')
    names ={
         'key1':'nameone',
         'key2':'nametwo',
         'key3':'namethree',
         'key4':'namefour',
         'key5':'namefive',
         'key6':'namesix',
         'key7':'hello java hello python',
   }
    
    return HttpResponse(template.render(context=names))


# for loop
mobilebrands= [
    {
        'productbrand' : 'samsung',
        'productcost' :10000.00,
        'productmodel':'note 10'
    },
    {
        'productbrand' :'redmi',
        'productcost' :11000.00,
        'productmodel' :'redmi 10'
    },
    {
        'productbrand' :'realme',
        'productcost':10000.00,
        'productmodel' : 'note 10'
    },
]
    
# if else
def getproducts(request):
   template=loader.get_template('getproducts.html')
   p={'mobilebrands' :mobilebrands}
   return HttpResponse(template.render(context=p))


# def getID(request):
#     template=loader.get_template('getID.html')
#     context={'id:',[]}
#     return HttpResponse(template.render[context])

def getID(request):
    context={'id:' :[]}
    return render(request,'getID.html',context)