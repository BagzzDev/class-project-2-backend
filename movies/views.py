from django.shortcuts import render


def index(request):
    """Render the homepage index."""
    return render(request, 'index.html')
