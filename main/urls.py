from django.conf.urls import patterns, url


urlpatterns = patterns('main.views.index',
    url(r'^$', 'index', name='index'),
    url(r'^redirect$', 'redirect_to', name='redirect')

)

urlpatterns += patterns('main.views.user',
    url(r'^login$', 'login', name='login'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^register$', 'register', name='register'),

    url(r'^users$', 'index'),
    url(r'^users/new$', 'new'),
    url(r'^users/create$', 'create'),
    url(r'^users/(<?P<id>.+)$', 'show'),
    url(r'^users/(<?P<id>.+)/edit$', 'edit'),
    url(r'^users/(<?P<id>.+)/update$', 'update'),
    url(r'^users/(<?P<id>.+)/destroy$', 'destroy'),
)

urlpatterns += patterns('main.views.product',
    url(r'^products$', 'index', name='products_index'),
    url(r'^products/new$', 'new', name='products_new'),
    url(r'^products/create$', 'create', name='products_create'),
    url(r'^products/transform$', 'transform', name="products_transform"),
    url(r'^products/(?P<id>.+)/edit$', 'edit', name='products_edit'),
    url(r'^products/(?P<id>.+)/update$', 'update', name='products_update'),
    url(r'^products/(?P<id>.+)/destroy$', 'destroy', name='products_destroy'),
    url(r'^products/(?P<id>.+)$', 'show', name='products_show'),
)