
from django.contrib import admin
from django.urls import path
from appone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userprofiledetails/',views.userprofiledetails),
    path('containsusername/',views.containsusername),
    path('icontainsusername/',views.containsusername),
    path('id_in/',views.id_in),
    path('startswith/',views.startswith),
    path('endswith/',views.endswith),
    path('idExact/',views.idExact),
    path('orOperator/',views.orOperator),
    path('andOperator/',views.andOperator),
    path('valuesMethod/',views.valuesMethod),
    path('valuesListMethod/',views.valuesListMethod),
    path('order_by/',views.order_by),
    path('avgsalary/',views.avgsalary),
    path('count/',views.count),
    path('max/',views.max),
    path('min/',views.min),
    path('sum/',views.sum),
    path('insertrecord/',views.insertrecord),
    path('saverecord/',views.saverecord),
    path('insertmultiplerecord/',views.insertmultiplerecord),
    path('updaterecord/',views.updaterecord),
    path('deleterecord/',views.deleterecord),
]
