# Generated by Django 5.0.4 on 2024-09-15 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_categorymodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='order_status',
            field=models.CharField(choices=[('ongoing', 'Ongoing'), ('accept', 'Accepted'), ('complete', 'Completed'), ('cancel', 'Cancelled'), ('reject', 'Rejected')], default='ongoing', max_length=50),
        ),
    ]
