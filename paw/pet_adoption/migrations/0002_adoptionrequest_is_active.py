# Generated by Django 4.1.13 on 2024-03-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet_adoption", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="adoptionrequest",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
