# Generated by Django 3.2.13 on 2022-08-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20220818_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='vehicle_reg',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
