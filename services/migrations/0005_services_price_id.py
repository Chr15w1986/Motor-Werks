# Generated by Django 3.2.13 on 2022-08-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_services_price_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='price_id',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
