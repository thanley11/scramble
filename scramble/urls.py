from django.conf.urls import patterns, include, url
from scramble import views
from django.conf import settings


urlpatterns = patterns('',
         url(r'^$', views.index, name='index'),
         url(r'^about/$', views.about, name='about'),
         url(r'^signin/$', views.signin, name='signin'),
         url(r'^register/$', views.register, name='register'),
         url(r'^logout/$', views.user_logout, name="logout"),
         url(r'^dashboard/$', views.dashboard, name="dashboard"),   
                url(r'^dashboard/new_scramble/$', views.new_scramble, name="new_scramble"),   
                url(r'^dashboard/friends/$', views.friends, name="friends"),
                url(r'^dashboard/history/$', views.history, name="history"),
                url(r'^dashboard/profile/$', views.profile, name="profile"),
                url(r'^dashboard/courses/$', views.courses, name="courses"),
         url(r'^new_scramble/$', views.new_scramble, name="new_scramble"), 
)