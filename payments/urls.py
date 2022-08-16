""" Payments and stripe url config file """
from django.urls import path
from .views import (PaymentsView, stripe_config,
                    create_checkout_session,
                    SuccessView, CancelledView,
                    stripe_webhook)

APP_NAME = 'payments'
urlpatterns = [
    path('', PaymentsView.as_view(), name='payments'),
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
    path('success/', SuccessView.as_view()),
    path('cancelled/', CancelledView.as_view()),
    path('webhook/', stripe_webhook),
]
