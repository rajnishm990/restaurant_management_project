from django.shortcuts import render
from products.model import Item

# Create your views here.

def HomePage(request):
    products = Item.objects.all()
    context = {"products":products}
    return render (request , "index.html", context)


