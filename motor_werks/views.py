""" Error handling Module """
from django.shortcuts import render


def custom_page_not_found(request, exception):
    """ 404 error view """
    data = {}
    return render(request, 'templates/404.html', data)


def custom_500_error(request, exception):
    """ 500 error view """
    data = {}
    return render(request, 'templates/500.html', data)


def custom_405_error(request, exception):
    """ 405 error view """
    data = {}
    return render(request, 'templates/405.html', data)


def custom_403_error(request, exception):
    """ 403 error view """
    data = {}
    return render(request, 'templates/403.html', data)
