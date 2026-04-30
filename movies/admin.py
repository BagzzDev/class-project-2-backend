from django.contrib import admin
from .models import (
    SocialLink,
    Tweet,
    Slider,
    Advertisement,
    Trailer,
    TrailerItem,
    Celebrity,
    News,
    MovieTheater,
    MovieTV
)

# Register your models here.
admin.site.register(SocialLink)
admin.site.register(Tweet)
admin.site.register(Slider)
admin.site.register(Advertisement)
admin.site.register(Trailer)
admin.site.register(TrailerItem)
admin.site.register(Celebrity)
admin.site.register(News)
admin.site.register(MovieTheater)
admin.site.register(MovieTV)

