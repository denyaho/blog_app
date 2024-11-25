# Generated by Django 4.2.15 on 2024-10-06 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("username", models.CharField(default="annonymous", max_length=30)),
                ("zipcode", models.CharField(default="", max_length=8)),
                ("prefecture", models.CharField(default="", max_length=10)),
                ("city", models.CharField(default="", max_length=100)),
                ("address", models.CharField(default="", max_length=200)),
            ],
        ),
    ]
