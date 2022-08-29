""" Payments app views file """

import stripe
import datetime
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from services.models import Services, ServiceHistory
from profiles.models import UserProfile


class PaymentsView(TemplateView):
    """ Renders the payments page """
    template_name = 'payments/payments.html'


class SuccessView(UserPassesTestMixin, TemplateView):
    """ Renders the payments success page """
    template_name = 'payments/success.html'

    def test_func(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        session_id = self.request.GET['session_id']
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            if session['payment_status'] == 'paid':
                line_item = stripe.checkout.Session.list_line_items(session_id, limit=1)
                service_name = line_item['data'][0].description
                service = Services.objects.get(service_name=service_name)
                order_date = datetime.datetime.now()
                ServiceHistory.objects.create(booked_by=self.request.user, service_type=service, order_date=order_date)
                return True
            else:
                return False
        except: 
            return False

class CancelledView(TemplateView):
    """ Renders the payments cancelled/failed page """
    template_name = 'payments/cancelled.html'


@csrf_exempt
# Taken from Testdriven.io
def stripe_config(request):

    if request.method == 'GET':
        stripe_config_data = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config_data, safe=False)
    return HttpResponse(status=400)


@csrf_exempt
# Taken from Testdriven.io
def create_checkout_session(request):

    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Extract the PK from the GET Pararameter (?pk=)
        service = Services.objects.get(pk=request.GET['pk'])
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'payments/success?session_id={CHECKOUT_SESSION_ID}',  # noqa
                cancel_url=domain_url + 'payments/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': service.price_id,
                        'quantity': 1,
                    }
                ],
                customer_email=request.user.email
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


# Stripe webhook handler
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:  # noqa
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:  # noqa
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")

    return HttpResponse(status=200)
