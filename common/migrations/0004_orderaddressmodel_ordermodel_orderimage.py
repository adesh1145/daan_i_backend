# Generated by Django 5.0.4 on 2024-05-23 03:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_categorymodel"),
        ("donar", "0006_addressmodel_is_default"),
        ("ngo", "0010_rename_accept_type_ngodetailmodel_accept_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderAddressModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("latitude", models.FloatField(default=0.0)),
                ("longitude", models.FloatField(default=0.0)),
                ("address", models.CharField(blank=True, max_length=255)),
                ("landmark", models.CharField(blank=True, max_length=255)),
                ("pincode", models.PositiveIntegerField(blank=True, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_city",
                        to="common.citymodel",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_state",
                        to="common.statemodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order Address",
                "verbose_name_plural": "Order Address",
                "db_table": "order_address",
            },
        ),
        migrations.CreateModel(
            name="OrderModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("order_id", models.CharField(max_length=255, null=True)),
                ("weight", models.FloatField(default=0.0)),
                ("description", models.CharField(max_length=255, null=True)),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("ongoing", "Ongoing"),
                            ("booked", "Booked"),
                            ("accept", "Accepted"),
                            ("complete", "Completed"),
                            ("cancel", "Cancelled"),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_category",
                        to="common.categorymodel",
                    ),
                ),
                (
                    "donar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_donar",
                        to="donar.userdetailmodel",
                    ),
                ),
                (
                    "drop_address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="drop_address",
                        to="common.orderaddressmodel",
                    ),
                ),
                (
                    "ngo",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_ngo",
                        to="ngo.ngodetailmodel",
                    ),
                ),
                (
                    "pickup_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pickup_address",
                        to="common.orderaddressmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order Table",
                "verbose_name_plural": "Order Table",
                "db_table": "order",
            },
        ),
        migrations.CreateModel(
            name="OrderImage",
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
                ("image", models.ImageField(upload_to="order_images/")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="common.ordermodel",
                    ),
                ),
            ],
        ),
    ]
