from django.conf.urls import patterns, include, url
from scramble import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
      url(r'^admin/', include(admin.site.urls)),
      url(r'^scramble/', include('scramble.urls')),
)
