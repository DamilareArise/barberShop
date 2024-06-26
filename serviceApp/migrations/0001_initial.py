# Generated by Django 5.0.4 on 2024-04-29 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("userApp", "0002_userprofile_hod"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                ("service_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "HOD",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userApp.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubService",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "HOD",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userApp.userprofile",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="serviceApp.service",
                    ),
                ),
            ],
        ),
    ]
