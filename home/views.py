from django.shortcuts import render
from products.model import Item 
from .models import Contact, MenuItem , Restaurant

# Create your views here.

def HomePage(request):

    sucess = False
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            Contact.objects.create(name=name, email=email)
        else:
            return Response({"detail": "name and email required"})
    try:
        products = Item.objects.all()
    except Exception as e:
        return Response({"Can't fetch teh Items , please try again later"})

    restaurant = Restaurant.objects.all()
    context = {"products":products, 'success':success , 'restaurant':restaurant}
    return render (request , "index.html", context)

def about_us(request):
    restaurant = Restaurant.objects.all()
    context = {"restaurant":restaurant}
    return render (request , 'about-us.html', context)

def menu_item_view(request):
    '''For displaying menu items '''
    menu_items = MenuItem.objects.all()
    context = {"menu_items": menu_items}
    return render(request , 'menu.html', context)


