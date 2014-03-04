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
    urls = [
        'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fre.taobao.com%2Feauction%3Fe%3DYqEM5tOqRXojmraEDZVrLrgfZyohkZIqorm1Hj1YRiaLltG5xFicOSZqewpHPyZzwmAG6lHaeulMpvv2sXr%252FoYxnJJLydRmxS%252B3KnK3RuPmB3ujUJI0OeA%253D%253D%26ptype%3D100010&k=e2e107a2b72ca1b1&c=un&b=alimm_0&p=mm_48677594_4312501_20302736',
        'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fre.taobao.com%2Feauction%3Fe%3DxAcQ%252B2lc%252BkPebLdhAWchHDqGMkej0GGCudTIvf5t7saLltG5xFicOSZqewpHPyZzwmAG6lHaeulMpvv2sXr%252FoYxnJJLydRmxS%252B3KnK3RuPmB3ujUJI0OeA%253D%253D%26ptype%3D100010&k=e2e107a2b72ca1b1&c=un&b=alimm_0&p=mm_48677594_4312501_20302736',
        'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fre.taobao.com%2Feauction%3Fe%3D15wjaXZH5D7ebLdhAWchHCbb%252FkjthnpolWsbAjdmP56LltG5xFicOSZqewpHPyZzwmAG6lHaeulMpvv2sXr%252FoYxnJJLydRmxS%252B3KnK3RuPmB3ujUJI0OeA%253D%253D%26ptype%3D100010&k=e2e107a2b72ca1b1&c=un&b=alimm_0&p=mm_48677594_4312501_20302736',
        'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fre.taobao.com%2Feauction%3Fe%3DWb66LQL2XDTebLdhAWchHEHknwN0zRJV2MCJOvlNXjyLltG5xFicOSZqewpHPyZzwmAG6lHaeulMpvv2sXr%252FoYxnJJLydRmxS%252B3KnK3RuPmB3ujUJI0OeA%253D%253D%26ptype%3D100010&k=e2e107a2b72ca1b1&c=un&b=alimm_0&p=mm_48677594_4312501_20302736'
    ]
    return redirect(urls[int(next_url)])
