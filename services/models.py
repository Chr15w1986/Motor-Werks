""" Services app models """

from django.db import models
from django.contrib.auth.models import User


class Services(models.Model):
    """ Services available model """
    service_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    price_id = models.CharField(max_length=200, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.service_name


class ServiceHistory(models.Model):
    """ User order history within the user profile """
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order_date = models.DateField(auto_now=False, blank=False, default=None)
    service_type = models.ForeignKey('Services', on_delete=models.CASCADE)
