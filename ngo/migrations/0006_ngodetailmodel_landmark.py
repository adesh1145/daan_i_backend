# Generated by Django 5.0.4 on 2024-05-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ngo", "0005_alter_ngodetailmodel_ngo_owner_ame"),
    ]

    operations = [
        migrations.AddField(
            model_name="ngodetailmodel",
            name="landmark",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
