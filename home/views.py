from django.shortcuts import render

from products.models import Product, Colour

# Create your views here.


def index(request):
    # A view to return the home page
    products = Product.objects.all()
    colours = Colour.objects.all()

    context = {
        'products': products,
        'colours': colours,
    }

    return render(request, 'home/index.html', context)
