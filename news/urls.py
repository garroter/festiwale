
from django.conf.urls import url
from news.views import Latest_news, Details

urlpatterns = [
    url(r'^aktualnosci/$', Latest_news.as_view(), name='latest_news'),
    url(r'^aktualnosci/strona/(?P<page>\d+)/$',
        Latest_news.as_view(), name='latest_news_pagination'),
    url(r'^artykul/(?P<url>[\w-]+)/$', Details.as_view(), name='news_details'),
]
