from django.shortcuts import render
# from .models import SocialLink, Tweet, Advertisement
from .models import (
    SocialLink,
    Tweet,
    Advertisement,
    Trailer
)


def index(request):
    """Render the homepage index."""
    social_links = SocialLink.objects.all()
    tweets = Tweet.objects.all()
    sidebar_ad = Advertisement.objects.filter(section='sidebar').first()
    news_banner_ad = Advertisement.objects.filter(section='latestnews').first()
    trailer = Trailer.objects.first()

    context = {
        'social_links': social_links,
        'tweets': tweets,
        'sidebar_ad': sidebar_ad,
        'news_banner_ad': news_banner_ad,
        'trailer': trailer,
    }
    return render(request, 'index.html', context)
