from django.conf.urls import patterns, include, url
from scramble import views
from django.conf import settings


urlpatterns = patterns('',
         url(r'^$', views.index, name='index'),
         url(r'^about/$', views.about, name='about'),
         url(r'^signin/$', views.signin, name='signin'),
         url(r'^register/$', views.register, name='register'),
)