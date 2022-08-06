from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicesView.as_view(), name='services'),
]
