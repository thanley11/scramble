from django.conf.urls import patterns, include, url
from scramble import views
from django.conf import settings


urlpatterns = patterns('',
         url(r'^$', views.index, name='index'),
)