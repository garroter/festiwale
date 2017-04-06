from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^najblizsze/$', views.Latest_festivals.as_view(), name='latest_festivals'),
    url(r'^najblizsze/strona/(?P<page>\d+)/$', views.Latest_festivals.as_view(), name='latest_festivals_pagination'),
    url(r'^(?P<url>[\w-]+)/$', views.details, name='festival_details'),
]