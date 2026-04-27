from django.db import models

# Create your models here.
class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    anchor_class = models.CharField(max_length=10)
    icon_class = models.CharField(max_length=30)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Tweet(models.Model):
    content = models.CharField(max_length=500)