from django.contrib import admin
from .models import SocialLink, Tweet

# Register your models here.
admin.site.register(SocialLink)
admin.site.register(Tweet)