# Generated by Django 3.2.13 on 2022-08-18 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='price_id',
        ),
    ]
