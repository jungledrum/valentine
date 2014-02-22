from django.shortcuts import render
from main.models.product import Products


def index(req):
    product = Products.objects.first()
    products = Products.objects
    context = {
        'product': product,
        'products': products
    }
    return render(req, 'index.html', context)
