from django.shortcuts import render, redirect
from main.models.product import Products


def index(req):
    product = Products.objects.first()
    products = Products.objects
    context = {
        'product': product,
        'products': products
    }
    return render(req, 'index.html', context)


def redirect_to(req):
    next_url = req.GET.get('url', 'http://www.weiaimeishi.com')
    return redirect(next_url)
