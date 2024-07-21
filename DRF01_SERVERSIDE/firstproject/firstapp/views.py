from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def get_products(request):
    emp={
        'product_id':2435,
        'product_name':'washing machine',
        'product_brand':'samsung',

        'specification':{
            'capacity':'7.5 kg',
            'type':'front load',
            'color':'white',
            'energy_rating':'5 star',
        },

        'pricing':{
            'currency_price':'INR',
            'amount':35000,

            'discount':{
                'amount':500,
                'expiry_date':'2024-8-30'
            }
        },
        'availability':{
              'instock':True,
              'stackcount':25,
              'estimated_delivery':2024-7-12
        }
    }
    return JsonResponse(emp)