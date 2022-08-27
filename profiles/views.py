""" Profile app views """

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from .forms import UserForm
from .models import UserProfile
from services.models import ServiceHistory


user = get_user_model()


class ProfileView(View):
    model = UserProfile
    form = UserForm
    template_name = 'profiles/profile.html'
    context = {'form': form}

    def form_valid(self, form):
        form.instance.booked_by = self.request.user
        return super().form_valid(form)


class UpdateProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Allows user to update personal profile
        via a pop up modal"""
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


class ServiceHistory(View):
    model = ServiceHistory
    fields = ('order_date',
              'service_type')
    template_name = 'profiles/profile.html'

    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.get(username=request.user.username)
        history = ServiceHistory.objects.filter(user=user)
        return render(request, self.template_name, {'user': user, 'history': history})


class DeleteProfile(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Allows user to delete personal profile """
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
    """ Renders a template to show user the deletion
        has been successful """
    model = User
    template_name = 'profiles/delete-success.html'
