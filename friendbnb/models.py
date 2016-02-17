from __future__ import unicode_literals

from django.conf import settings
from django.db import models

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Listing(models.Model):
    name = models.CharField(max_length=200)
    main_image = models.ImageField(blank=True)
    location = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name='images',
            on_delete=models.CASCADE)
    image = models.ImageField()

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,
            help_text='The date the review was submitted')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.SET(get_sentinel_user),
            help_text='The author of the review')
    rating = models.IntegerField(blank=True)
    text = models.TextField(blank=True)

    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
