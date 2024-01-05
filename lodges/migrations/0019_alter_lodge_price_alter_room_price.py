# Generated by Django 4.2 on 2023-12-26 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0018_lodge_video_alter_lodge_slug_alter_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodge',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]