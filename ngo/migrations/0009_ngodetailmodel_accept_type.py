# Generated by Django 5.0.4 on 2024-05-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_categorymodel"),
        ("ngo", "0008_ngodetailmodel_registration_step"),
    ]

    operations = [
        migrations.AddField(
            model_name="ngodetailmodel",
            name="accept_type",
            field=models.ManyToManyField(to="common.categorymodel"),
        ),
    ]
