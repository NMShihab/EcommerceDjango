from django.shortcuts import render
from django.views.generic import  ListView,DetailView

from Shop.models import Product

# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'Shop/home.html'
