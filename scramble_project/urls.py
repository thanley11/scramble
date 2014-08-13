from django.conf.urls import patterns, include, url
from scramble import views
from snippets import views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
      url(r'^admin/', include(admin.site.urls)),
      url(r'^', include('scramble.urls')),
      url(r'^snippets/', include('snippets.urls')),
      url(r'^account/', include('django.contrib.auth.urls')),
)

if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )
