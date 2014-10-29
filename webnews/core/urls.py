from django.conf.urls import patterns, url

urlpatterns = patterns('webnews.core.views',
    url(r'^$', 'home', name='home'),
)
