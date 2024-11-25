# Generated by Django 4.2.15 on 2024-11-20 14:39

from django.db import migrations, models
import mysite.models.profile_models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0002_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="images",
            field=models.ImageField(
                blank=True,
                default="",
                upload_to=mysite.models.profile_models.upload_image_to,
            ),
        ),
    ]
