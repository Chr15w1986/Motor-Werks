""" Profiles app url config file """
from django.urls import path
from .views import ProfileView

APP_NAME = 'profiles'
urlpatterns = [
    path('', ProfileView.as_view(), name='my-profile'),
]