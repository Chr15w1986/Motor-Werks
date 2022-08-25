""" Profile app views """

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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
    fields = ('first_name',
              'last_name',
              'email',
              'vehicle_reg',
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


class DeleteProfile(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = User
    template_name = 'profiles/delete-profile.html'

    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.id)
        user.delete()

        return HttpResponseRedirect(reverse('delete-success'))

    def test_func(self):
        self.object = self.get_object()
        return self.object == self.request.user


class DeleteSuccess(TemplateView):

    model = User
    template_name = 'profiles/delete-success.html'
