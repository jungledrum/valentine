from django.conf.urls import patterns, url


urlpatterns = patterns('main.views.index',
    url(r'^$', 'index'),
    url(r'^hi$', 'hi')
)

urlpatterns = patterns('main.views.user',
    url(r'^users$', 'index'),
    url(r'^users/new$', 'new'),
    url(r'^users/create$', 'create'),
    url(r'^users/(<?P<id>.+)$', 'show'),
    url(r'^users/(<?P<id>.+)/edit$', 'edit'),
    url(r'^users/(<?P<id>.+)/update$', 'update'),
    url(r'^users/(<?P<id>.+)/destroy$', 'destroy'),
)