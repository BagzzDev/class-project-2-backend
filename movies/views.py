from django.shortcuts import render
from .models import SocialLink, Tweet


def index(request):
    """Render the homepage index."""
    social_links = SocialLink.objects.all()
    tweets = Tweet.objects.all()

    context = {
        'social_links': social_links,
        'tweets': tweets,
    }
    return render(request, 'index.html', context)
