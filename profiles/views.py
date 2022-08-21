""" Profile app views """

from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserForm
from .models import UserProfile


class ProfileView(TemplateView):
    template_name = 'profiles/profile.html'


class UpdateProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = UserProfile
    form = UserForm
    template_name = 'profiles/update-profile.html'
    success_url = reverse_lazy('update-profile')
    context = {'form': form}

    def test_func(self):
        self.object = self.get_object()
        return self.object.author == self.request.user
