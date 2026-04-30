from django.shortcuts import render
# from .models import SocialLink, Tweet, Advertisement
from .models import (
    SocialLink,
    Tweet,
    Advertisement,
    Trailer,
    MovieTV,
    Celebrity,
    News,
    Slider,
)


def index(request):
    """Render the homepage index."""
    social_links = SocialLink.objects.all()
    tweets = Tweet.objects.all()
    slider = Slider.objects.all()
    sidebar_ad = Advertisement.objects.filter(section='sidebar').first()
    news_banner_ad = Advertisement.objects.filter(section='latestnews').first()
    trailer = Trailer.objects.first()
    celebrities = Celebrity.objects.all()[:4]
    featured_news = News.objects.filter(section='featured').first()
    more_news = News.objects.filter(section='more').order_by('-id')[:2] # sort newest records first then take 2

    context = {
        'social_links': social_links,
        'tweets': tweets,
        'slider': slider,
        'sidebar_ad': sidebar_ad,
        'news_banner_ad': news_banner_ad,
        'trailer': trailer,
        'celebrities': celebrities,
        'featured_news': featured_news,
        'more_news': more_news,

    }
    return render(request, 'index.html', context)

