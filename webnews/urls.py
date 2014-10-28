from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^accounts/', include('webnews.accounts.urls', namespace='accounts')),

    url(r'^admin/', include(admin.site.urls)),
)
