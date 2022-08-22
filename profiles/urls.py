""" Profiles app url config file """
from django.urls import path
from .views import ProfileView, UpdateProfile

APP_NAME = 'profiles'
urlpatterns = [
    path('', ProfileView.as_view(), name='my-profile'),
    path('update/<int:pk>/', UpdateProfile.as_view(), name='update-profile'),
]
