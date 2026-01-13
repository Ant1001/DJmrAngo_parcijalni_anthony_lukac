from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['name', 'vat_id', 'street', 'city', 'country']
    success_url = '/customers/'

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['name', 'vat_id', 'street', 'city', 'country']
    success_url = '/customers/'

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = '/customers/'
