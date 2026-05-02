from django.shortcuts import redirect, render
# from .models import SocialLink, Tweet, Advertisement
from .models import (
    SocialLink,
    Tweet,
    Advertisement,
    Trailer,
    TrailerItem,
    MovieTV,
    Celebrity,
    News,
    Slider,
    MovieTheater,
)


def index(request):
    """Render the homepage index."""
    social_links = SocialLink.objects.all()
    tweets = Tweet.objects.all()
    slider = Slider.objects.all()
    sidebar_ad = Advertisement.objects.filter(section='sidebar').first()
    news_banner_ad = Advertisement.objects.filter(section='latestnews').first()
    trailer = Trailer.objects.first()
    trailer_items = TrailerItem.objects.all()
    celebrities = Celebrity.objects.all()[:4]
    featured_news = News.objects.filter(section='featured').first()
    more_news = News.objects.filter(section='more').order_by('-id')[:2] # sort newest records first then take 2
    movietheater_popular = MovieTheater.objects.filter(type='popular')
    movietheater_comingsoon = MovieTheater.objects.filter(type='coming-soon')

    popular_tv = MovieTV.objects.filter(type="popular")
    coming_soon_tv = MovieTV.objects.filter(type="coming-soon")
    context = {
        'social_links': social_links,
        'tweets': tweets,
        'slider': slider,
        'sidebar_ad': sidebar_ad,
        'news_banner_ad': news_banner_ad,
        'trailer': trailer,
        'trailer_items': trailer_items,
        'celebrities': celebrities,
        'featured_news': featured_news,
        'more_news': more_news,
        'movietv_popular': movietheater_popular,
        'movietv_comingsoon': movietheater_comingsoon,
        'popular_tv' : popular_tv,
        'coming_soon_tv' : coming_soon_tv,


    }
    return render(request, 'index.html', context)

def movie_single(request):
    return render(request, 'moviesingle.html')


def newsletter(request):
    email = request.POST.get('email')

    context = {
        'email': email
    }

    return render(request, 'newsletter.html', context)
