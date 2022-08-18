from django.db import models


class Services(models.Model):

    service_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    price_id = models.CharField(max_length=200, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.service_name
