""" Admin config file for services app """
from django.contrib import admin
from .models import Services, ServiceHistory


admin.site.register(Services)
admin.site.register(ServiceHistory)
