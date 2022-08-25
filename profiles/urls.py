""" Profiles app url config file """
from django.urls import path
from .views import (ProfileView,
                    UpdateProfile,
                    DeleteProfile,
                    DeleteSuccess)

APP_NAME = 'profiles'
urlpatterns = [
    path('', ProfileView.as_view(), name='my-profile'),
    path('update/<int:pk>/', UpdateProfile.as_view(), name='update-profile'),
    path('delete/<int:pk>/', DeleteProfile.as_view(), name='delete-profile'),
    path('delete_success/', DeleteSuccess.as_view(), name='delete-success'),
]
