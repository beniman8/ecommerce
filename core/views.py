from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Item, Order,OrderItem



class HomeView(ListView):
    model = Item
    paginate_by = 10
template_name = "home.html"