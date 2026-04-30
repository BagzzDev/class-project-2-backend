from django.shortcuts import render
from .models import SocialLink, Tweet, MovieTV


def index(request):
    """Render the homepage index."""
    social_links = SocialLink.objects.all()
    tweets = Tweet.objects.all()
    movie_tvs = MovieTV.objects.all()

    context = {
        'social_links': social_links,
        'tweets': tweets,
        'movie_tvs': movie_tvs,
    }
    return render(request, 'index.html', context)

