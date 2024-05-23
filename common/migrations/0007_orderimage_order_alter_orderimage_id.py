# Generated by Django 5.0.4 on 2024-05-23 03:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0006_remove_ordermodel_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderimage",
            name="order",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="common.ordermodel",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="orderimage",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
