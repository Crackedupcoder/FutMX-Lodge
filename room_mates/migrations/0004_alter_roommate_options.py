# Generated by Django 4.2 on 2023-12-26 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_mates', '0003_roommate_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roommate',
            options={'ordering': ['-created_at']},
        ),
    ]
