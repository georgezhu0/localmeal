from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from foodcycle import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^clients/', include('food.urls')),
    url(r'^drivers/', include('food.driveurls')),
    url(r'^$', views.index, name='index'),

 )

#media
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )



