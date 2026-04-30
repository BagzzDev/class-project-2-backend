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


class Slider(models.Model):
    image_src = models.CharField(max_length=200)
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=50)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)


class Advertisement(models.Model):
    section = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()

class Trailer(models.Model):
    trailer_URL = models.CharField(max_length=200)

class TrailerItem(models.Model):
    img_src = models.CharField(max_length=200)
    img_alt = models.CharField(max_length=100)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)

class Celebrity(models.Model):
    anchor_url = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    celebrity_url = models.CharField(max_length=200)
    celebrity_name = models.CharField(max_length=50)
    celebrity_type = models.CharField(max_length=20)

class News(models.Model):
    section = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_alt = models.CharField(max_length=100)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    time = models.CharField(max_length=20)

class MovieTheater(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)

class MovieTV(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)
