# Generated by Django 4.2 on 2023-11-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0003_room_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image1',
            field=models.ImageField(blank=True, upload_to='rooms/'),
        ),
        migrations.AddField(
            model_name='room',
            name='image2',
            field=models.ImageField(blank=True, upload_to='rooms/'),
        ),
        migrations.AddField(
            model_name='room',
            name='image3',
            field=models.ImageField(blank=True, upload_to='rooms/'),
        ),
        migrations.AddField(
            model_name='room',
            name='image4',
            field=models.ImageField(blank=True, upload_to='rooms/'),
        ),
        migrations.AddField(
            model_name='room',
            name='image5',
            field=models.ImageField(blank=True, upload_to='rooms/'),
        ),
    ]
