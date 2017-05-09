from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from news.models import News
from .models import Festival, Artist
from sliders.models import Slide


def home(request):

    slider = Slide.objects.filter(
        slider__home=True, slider__status=True, status=True).all()
    news = News.objects.all()[:5]
    festivals_pl = Festival.objects.filter(country=178).all()[:10]
    festivals_all = Festival.objects.exclude(country=178).all()[:10]
    artists = Artist.objects.all()[:10]
    return render(request, 'index.html', {'festivals_pl': festivals_pl, 'festivals_all': festivals_all, 'news': news, 'slider': slider, 'artists': artists})


def festival_details(request, url):

    festival = get_object_or_404(Festival, url=url)
    news = News.objects.filter(festivals=festival.pk).all()
    return render(request, 'festivals/details.html', {'festival': festival, 'news': news})


class Latest_festivals(ListView):
    model = Festival
    ordering = ['-pub_date_start']
    template_name = 'festivals/list.html'
    context_object_name = 'festivals'
    paginate_by = settings.PAGINATION


class Festivals_tags(ListView):
    model = Festival
    ordering = ['-pub_date_start']
    template_name = 'festivals/list.html'
    context_object_name = 'festivals'
    paginate_by = settings.PAGINATION

    def get_queryset(self):

        return Festival.objects.filter(tags__url__in=[self.kwargs['url']])


class Artists_list(ListView):
    model = Artist
    query_set = Artist.objects.filter(status=True)
    template_name = 'artists/list.html'
    context_object_name = 'artists'
    paginate_by = settings.PAGINATION


class Artist_details(DetailView):

    model = Artist
    template_name = 'artists/details.html'
    context_object_name = 'artist'
    slug_field = 'url'
    slug_url_kwarg = 'url'
