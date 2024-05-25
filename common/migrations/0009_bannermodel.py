# Generated by Django 5.0.4 on 2024-05-25 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0008_remove_ordermodel_drop_address_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BannerModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("image", models.ImageField(upload_to="")),
            ],
            options={
                "verbose_name": "Banner",
                "verbose_name_plural": "banners",
                "db_table": "banner",
            },
        ),
    ]
