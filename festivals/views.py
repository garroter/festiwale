from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from news.models import News
from .models import Festival, Artist
from sliders.models import Slide


def home(request):

    slider = Slide.objects.filter(slider__home=True, slider__status=True, status=True).all()
    news = News.objects.all()[:5]
    festivals_pl = Festival.objects.filter(country=178).all()[:10]
    festivals_all = Festival.objects.exclude(country=178).all()[:10]
    artists = Artist.objects.all()[:10]
    return render(request, 'index.html', {'festivals_pl': festivals_pl, 'festivals_all': festivals_all, 'news': news, 'slider': slider, 'artists': artists})


def details(request, url):
    
    festival = get_object_or_404(Festival, url=url)
    news = News.objects.filter(festivals=festival.pk).all()
    return render(request, 'festivals/details.html', {'festival': festival, 'news': news})


class Latest_festivals(ListView):
    model = Festival
    ordering = ['-pub_date_start']
    template_name = 'festivals/list.html' 
    context_object_name = 'festivals'
    paginate_by = settings.PAGINATION