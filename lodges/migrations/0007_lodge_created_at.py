# Generated by Django 4.2 on 2023-11-27 12:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0006_alter_room_options_alter_lodge_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodge',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
