from django.conf.urls import patterns, url


urlpatterns = patterns('main.views.index',
    url(r'^$', 'index'),
    url(r'^hi$', 'hi')
)
