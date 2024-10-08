# Generated by Django 5.0.4 on 2024-06-01 03:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0012_ordermodel_donar_address"),
        ("donar", "0008_addressmodel_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordermodel",
            name="donar",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_donar",
                to="donar.userdetailmodel",
            ),
            preserve_default=False,
        ),
    ]
