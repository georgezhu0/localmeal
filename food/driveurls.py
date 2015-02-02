from django.conf.urls import patterns, url
from food import views

urlpatterns = patterns('',
    url(r'^$', views.map, name='driverlog'),
    url(r'^register/$', views.driver_register, name='register'),
    url(r'^login/$', views.driver_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    )
