""" Profile app views """
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import UserForm


class ProfileView(TemplateView):
    template_name = 'profiles/profile.html'


@login_required
def userpage(request):
    user_form = UserForm(instance=request.user)

    return render(
                  request=request, template_name="profiles/profile.html",
                  context={"user": request.user, "user_form": user_form, }
        )
