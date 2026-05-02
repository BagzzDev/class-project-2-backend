from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('moviesingle/', views.movie_single, name='movie_single'),
    path('newsletter/', views.newsletter, name='newsletter'),
]
        