# Generated by Django 5.0.4 on 2024-04-18 12:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone_number", models.CharField(max_length=15)),
                ("address", models.CharField(max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Others", "Others"),
                        ],
                        max_length=50,
                    ),
                ),
                ("date_of_birth", models.CharField(max_length=11)),
                ("portfolio", models.FileField(null=True, upload_to="portfolio/")),
                (
                    "nationality",
                    models.CharField(
                        choices=[
                            ("Nigeria", "Nigeria"),
                            ("United State", "United State"),
                            ("Others", "Others"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "displayPicture",
                    models.ImageField(null=True, upload_to="profile_picture/"),
                ),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("Admin", "Admin"),
                            ("Supervisor", "Supervisor"),
                            ("Hair Cut Specialist", "Hair Cut Specialist"),
                            ("Beard Specialist", "Beard Specialist"),
                            ("Hair Color Specialist", "Hair Color Specialist"),
                        ],
                        max_length=255,
                    ),
                ),
                ("staff", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]