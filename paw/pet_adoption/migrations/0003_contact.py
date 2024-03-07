# Generated by Django 4.1.13 on 2024-03-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet_adoption", "0002_adoptionrequest_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=35)),
                ("email", models.EmailField(max_length=100)),
                ("phone_number", models.CharField(max_length=50)),
                ("subject", models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]