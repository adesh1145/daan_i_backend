# Generated by Django 5.0.4 on 2024-05-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ngo", "0002_alter_ngodetailmodel_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ngodetailmodel",
            name="pincode",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
