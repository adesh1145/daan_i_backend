# Generated by Django 5.0.4 on 2024-05-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donar", "0006_addressmodel_is_default"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userdetailmodel",
            name="address",
        ),
        migrations.AddField(
            model_name="userdetailmodel",
            name="bio",
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
