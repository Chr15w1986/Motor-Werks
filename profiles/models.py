""" Profile app models """

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """ User profile models """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, blank=False, default=None)
    last_name = models.CharField(max_length=25, blank=False, default=None)
    email = models.CharField(max_length=40, blank=False, default=None)
    street_address1 = models.CharField(max_length=60, blank=False, default=None)  # noqa
    street_address2 = models.CharField(max_length=60, blank=True, default=None)
    town_or_city = models.CharField(max_length=40, blank=False, default=None)
    county = models.CharField(max_length=40, blank=False, default=None)
    postcode = models.CharField(max_length=20, blank=False, default=None)
    phone_number = models.CharField(max_length=20, blank=False, default=None)
    vehicle_reg = models.CharField(max_length=8, blank=False, default=None)

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
