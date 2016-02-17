from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', context=locals())

def about(request):
    return render(request, 'about.html', context=locals())
