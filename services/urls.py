""" Url config file for services app """
from django.urls import path
from .views import SingleServiceDetail, AllServicesView

APP_NAME = 'services'
urlpatterns = [
    path('', AllServicesView.as_view(), name='services'),
    path('services_detail/<int:pk>/', SingleServiceDetail.as_view(),
         name='services_detail'),
]
