from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Services


class ServicesView(ListView):
    model = Services
    template_name = 'services/major.html'
    success_url = reverse_lazy('major')
    queryset = Services.objects.all().order_by('service_name')
