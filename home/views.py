from django.shortcuts import render
from news.models import News
from festivals.models import Festival, Artist
from sliders.models import Slide

def home(request):

    slider = Slide.objects.filter(slider__home=True, slider__status=True, status=True).all()
    news = News.objects.all()[:5]
    festivals_pl = Festival.objects.filter(country=178).all()[:10]
    festivals_all = Festival.objects.exclude(country=178).all()[:10]
    artists = Artist.objects.all()[:10]
   
    return render(request, 'home/index.html', {'festivals_pl': festivals_pl, 'festivals_all': festivals_all, 'news': news, 'slider': slider, 'artists': artists})

