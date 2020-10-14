from django.shortcuts import render

#import views
from django.views.generic import  ListView,DetailView

# import  mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# import models
from Shop.models import Product

# Home page view
class Home(ListView):
    model = Product
    template_name = 'Shop/home.html'


# Detail page view
class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "Shop/detail.html"