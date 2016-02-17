from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

@python_2_unicode_compatible
class Listing(models.Model):
    name = models.CharField(max_length=200)
    main_image = models.ImageField(blank=True, null=True, upload_to='images')
    location = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name='images',
            on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return 'Image for %s' % self.listing.name

@python_2_unicode_compatible
class Review(models.Model):
    listing = models.ForeignKey(Listing, related_name='reviews',
            on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,
            help_text='The date the review was submitted')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
            related_name='reviews',
            on_delete=models.SET(get_sentinel_user),
            help_text='The author of the review')
    rating = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        get_latest_by = 'date'

    def __str__(self):
        return 'Review for %s by %s on %s, %d stars' % (
                self.listing.name,
                self.author.get_full_name(),
                self.date.date().isoformat(),
                self.rating)
