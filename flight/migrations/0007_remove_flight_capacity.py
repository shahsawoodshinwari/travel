# Generated by Django 4.1 on 2022-09-17 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flight", "0006_flight_airplane"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="flight",
            name="capacity",
        ),
    ]
