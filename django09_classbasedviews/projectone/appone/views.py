from django.shortcuts import render
from appone.models import product
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class productlistview(ListView):
      model=product


# Listview and Detailviews are two class based-views.
# when we use Listview which refers to view to display multiple intances of table in database.
# we only specify the model name which apply List view

class productDetailview(DetailView):

      model=product 

class productCreateview(CreateView):
      model=product
      fields='__all__'

      success_url=reverse_lazy('products')

class productUpdateview(UpdateView):
      model=product
      fields='__all__'

      success_url=reverse_lazy('products')

class productDeleteview(DeleteView):
      model=product
      success_url=reverse_lazy('products')
