""" Home page views """

from django.shortcuts import render


def index(request):
    """ View to return the home/landing page """
    return render(request, 'home/index.html')
