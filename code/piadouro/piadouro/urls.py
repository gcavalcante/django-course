from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'piadouro_website.views.home', name='home'),    
    #Admin
    url(r'^admin/', include(admin.site.urls)),
)
