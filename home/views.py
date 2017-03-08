from django.shortcuts import render
from news.models import News
from festivals.models import Festival

def home(request):

    news = News.objects.all()[:5]
    festivals = Festival.objects.all()

    return render(request, 'home/index.html', {'festivals': festivals,'news': news})

