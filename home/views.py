from django.shortcuts import render
from products.model import Item
from .forms import ContactForm

# Create your views here.

def HomePage(request):
    success = False
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()
    else:
        form = ContactForm()
    products = Item.objects.all()
    context = {"products":products , 'form':'form', 'success':success}
    return render (request , "index.html", context)



