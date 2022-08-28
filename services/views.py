""" Views file for services app """
from django.views.generic import DetailView, ListView
from .models import Services


class AllServicesView(ListView):
    """ Service list view for all available services"""
    model = Services
    template_name = 'services/services.html'
    context_object_name = 'services'
    queryset = Services.objects.all().order_by('service_name')


class SingleServiceDetail(DetailView):
    """ SingleService view to allow users to view the
        individual service chosen in more detail"""
    model = Services
