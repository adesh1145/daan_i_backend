# Generated by Django 5.0.4 on 2024-05-20 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ngo", "0009_ngodetailmodel_accept_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ngodetailmodel",
            old_name="accept_type",
            new_name="accept_category",
        ),
    ]
