# Generated by Django 5.0.4 on 2024-04-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("serviceApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="sevice_image",
            field=models.ImageField(blank=True, null=True, upload_to="service-image/"),
        ),
        migrations.AddField(
            model_name="subservice",
            name="subSevice_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="sub-service-image/"
            ),
        ),
    ]
