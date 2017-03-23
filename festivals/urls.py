from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<url>[\w-]+)/$', views.details, name='details'),
]