from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Services


# class ServicesView(ListView):
#     model = Services
#     template_name = 'services/<int:pk>/'
#     context_object_name = 'services'
#     context = {'services/<int:pk>': Services}
#     paginate_by = 1

# class SingleServiceView(DetailView):
#     model = Services
#     template_name = 'services/'
#     context = {'services/<int:pk>': Services}


class AllServicesView(ListView):
    """ Service list view for all available services"""
    model = Services
    template_name = 'services/services.html'
    context_object_name = 'services'
    queryset = Services.objects.all().order_by('service_name')
    paginate_by = 5


class SingleServiceDetail(DetailView):
    """ SingleService view to allow users to view the
        individual service chosen in more detail"""
    model = Services

    def services_detail(self, request, service_id):

        services = get_object_or_404(Services, pk=service_id)

        context = {
            'services': services,
        }

        return render(request, 'services/services_detail.html', context)
