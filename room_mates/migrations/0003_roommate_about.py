# Generated by Django 4.2 on 2023-12-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_mates', '0002_roommate_created_at_roommate_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommate',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
