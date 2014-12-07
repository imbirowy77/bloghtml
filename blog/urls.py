from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^onas/$', 'blog.views.onas', name='onas'),
    url(r'^content/$', 'blog.views.content', name='content'),
    url(r'^kontakt/$', 'blog.views.kontakt', name='kontakt'),
    url(r'^admin/', include(admin.site.urls)),
)
