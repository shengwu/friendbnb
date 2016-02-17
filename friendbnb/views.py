from django.shortcuts import render

from .models import *

def home(request):
    listings = Listing.objects.order_by('-reviews__date')
    return render(request, 'home.html', context=locals())

def about(request):
    return render(request, 'about.html', context=locals())
