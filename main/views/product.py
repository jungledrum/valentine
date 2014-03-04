from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from main.models.product import Products
from lib.crawler import crawl


def index(req):
    return HttpResponse('hah')


def show(req, id):
    if req.is_ajax():
        product = Products.objects.with_id(id)
        return HttpResponse(product.to_json(), mimetype='application/json')
    else:
        product = Products.objects.with_id(id)
        products = Products.objects
        context = {
            'product': product,
            'products': products
        }
        return render(req, 'index.html', context)


@login_required
def new(req):
    print req.user
    return render(req, 'new.html')


@login_required
def create(req):
    form = req.POST.dict()
    print form
    product = Products(**form)

    images = req.POST.getlist('images', [])
    images = map(lambda x: x.replace('60x60', '360x360') ,images)
    product.images = images

    product.created_at = datetime.now()
    product.updated_at = datetime.now()
    product.save()
    return redirect(reverse('index'))


@login_required
def edit(req):
    pass


@login_required
def update(req):
    pass


@login_required
def destroy(req):
    pass


@login_required
def transform(req):
    url = req.POST.get('url', '')
    product = crawl(url)
    return render(req, 'new.html', {'product': product})
