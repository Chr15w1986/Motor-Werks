""" Profile app views """

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserForm
from .models import UserProfile


user = get_user_model()


class ProfileView(TemplateView):
    model = UserProfile
    form = UserForm
    template_name = 'profiles/profile.html'
    context = {'form': form}


class UpdateProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = UserProfile
    fields = ('vehicle_reg',
              'first_name',
              'last_name',
              'email',
              'street_address1',
              'street_address2',
              'town_or_city',
              'county',
              'postcode',
              'phone_number')
    template_name = 'profiles/profile.html'

    def post(self, request, pk, *args, **kwargs):
        user = request.user.userprofile.id
        user_form = UserForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid():
            user_form.instance.user = request.user
            user_form.save()
        return HttpResponseRedirect(reverse('update-profile', args=[user]))

    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user
