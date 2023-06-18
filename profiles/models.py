""" Profile app models """

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """ User profile models """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    email = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=60, blank=False)  # noqa
    street_address2 = models.CharField(max_length=60, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    vehicle_reg = models.CharField(max_length=8, blank=False)

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
