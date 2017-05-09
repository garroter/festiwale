from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^najblizsze/$', views.Latest_festivals.as_view(), name='latest_festivals'),
    url(r'^najblizsze/strona/(?P<page>\d+)/$',
        views.Latest_festivals.as_view(), name='latest_festivals_pagination'),
    url(r'^tag/(?P<url>[\w-]+)/$',
        views.Festivals_tags.as_view(), name='festivals_tags'),

    url(r'^artysta/(?P<url>[\w-]+)/$',
        views.Artist_details.as_view(), name='artist_details'),
    url(r'^artysci/$', views.Artists_list.as_view(), name='artists_list'),
    url(r'^artysci/strona/(?P<page>\d+)/$',
        views.Artists_list.as_view(), name='artists_list_pagination'),

    url(r'^(?P<url>[\w-]+)/$', views.festival_details,
        name='festival_details'),
]
