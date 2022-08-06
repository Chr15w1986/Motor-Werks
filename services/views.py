from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Services


class ServicesView(ListView):
    template_name = 'services/services.html'
    model = Services
    context_object_name = 'services'

    def get_queryset(self):
        return Services.objects.all()
