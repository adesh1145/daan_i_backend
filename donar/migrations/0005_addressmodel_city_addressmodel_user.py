# Generated by Django 5.0.4 on 2024-05-21 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_categorymodel"),
        ("donar", "0004_addressmodel_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="addressmodel",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="city",
                to="common.citymodel",
            ),
        ),
        migrations.AddField(
            model_name="addressmodel",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="donar",
                to="donar.userdetailmodel",
            ),
            preserve_default=False,
        ),
    ]
