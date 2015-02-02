from django.conf.urls import patterns, url
from food import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^college/$', views.college, name='college'),
		url(r'^add_college/$', views.add_college, name='add_college'), # NEW MAPPING!
    url(r'^college/(?P<college_name_url>\w+)$', views.college, name='college'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^log/$', views.log, name='log'),
    url(r'^order/swat$', views.order_swat, name='order'),
    url(r'^order/hav$', views.order_hav, name='order'),
    url(r'^order/thankyou$', views.thankyou, name='THANKS'),
    url(r'^map/$', views.map, name='map'),
    )
