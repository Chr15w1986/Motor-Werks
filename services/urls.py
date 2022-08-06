from django.urls import path
from . import views

APP_NAME = 'services'
urlpatterns = [
    path('', views.ServicesView.as_view(), name='services'),
    path('major/', views.ServicesView.as_view(), name='major'),
    path('minor/', views.ServicesView.as_view(), name='minor'),
    path('suspension/', views.ServicesView.as_view(), name='suspension'),
    path('brakes/', views.ServicesView.as_view(), name='brakes'),
    path('tyres/', views.ServicesView.as_view(), name='tyres'),
]
