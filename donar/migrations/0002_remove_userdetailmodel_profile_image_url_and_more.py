# Generated by Django 5.0.4 on 2024-05-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetailmodel',
            name='profile_image_url',
        ),
        migrations.AddField(
            model_name='userdetailmodel',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
