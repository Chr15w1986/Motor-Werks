from django.urls import path
from . import views

APP_NAME = 'services'
urlpatterns = [
    path('', views.AllServicesView.as_view(), name='services'),
    path('services_detail/<int:pk>/', views.SingleServiceDetail.as_view(),
         name='services-detail'),
]
