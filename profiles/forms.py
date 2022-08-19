from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ['user',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'county',
                  'postcode',
                  'phone_number']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'county',
                  'postcode',
                  'phone_number']
