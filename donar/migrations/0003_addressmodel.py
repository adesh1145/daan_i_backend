# Generated by Django 5.0.4 on 2024-05-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donar", "0002_remove_userdetailmodel_profile_image_url_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AddressModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("latitude", models.FloatField(default=0.0)),
                ("longitude", models.FloatField(default=0.0)),
                ("address", models.CharField(blank=True, max_length=255)),
                ("landmark", models.CharField(blank=True, max_length=255)),
                ("pincode", models.PositiveIntegerField(blank=True, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Donar Address",
                "verbose_name_plural": "Donar Address",
                "db_table": "donar_address",
            },
        ),
    ]
