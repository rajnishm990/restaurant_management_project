from django.shortcuts import render
from products.model import Item 
from .models import Contact

# Create your views here.

def HomePage(request):

    sucess = False
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            Contact.objects.create(name=name, email=email)
    
    products = Item.objects.all()
    context = {"products":products, 'success':success}
    return render (request , "index.html", context)


