# Generated by Django 4.2 on 2023-11-25 17:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0002_room_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
