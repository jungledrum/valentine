from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from main.models.product import Products
from lib.crawler import crawl


@login_required
def index(req):
    products = Products.objects
    return render(req, 'products/index.html', {'products': products})


def show(req, id):
    if req.is_ajax():
        product = Products.objects.with_id(id)
        return render(req, 'products/_detail.html', {'product': product})
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
    return render(req, 'products/new.html')


@login_required
def create(req):
    form = req.POST.dict()
    product = Products(**form)

    images = req.POST.getlist('images', [])
    images = map(lambda x: x.replace('60x60', '360x360') ,images)
    product.images = images

    product.created_at = datetime.now()
    product.updated_at = datetime.now()
    product.save()
    return redirect('products_index')


@login_required
def edit(req, id):
    product = Products.objects.with_id(id)
    return render(req, 'products/edit.html', {'product': product})


@login_required
def update(req, id):
    form = req.POST.dict()
    images = req.POST.getlist('images', [])
    form['images'] = images
    form['updated_at'] = datetime.now()

    def _add_set(form):
        d = {}
        for k,v in form.iteritems():
            if k == 'csrfmiddlewaretoken':
                continue
            k = 'set__' + k
            d[k] = v
        return d
    form = _add_set(form)

    product = Products.objects.with_id(id)
    product.update(**form)
    return redirect('products_index')


@login_required
def destroy(req, id):
    product = Products.objects.with_id(id)
    product.delete()
    return redirect('products_index')


@login_required
def transform(req):
    url = req.POST.get('url', '')
    product = crawl(url)
    return render(req, 'products/new.html', {'product': product})
