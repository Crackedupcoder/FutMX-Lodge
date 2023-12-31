# Generated by Django 4.2 on 2024-01-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0022_alter_lodge_cover_image_alter_lodgeimage_image_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='lodge',
            index=models.Index(fields=['-created_at', 'name', 'campus', 'area', 'water', 'light', 'price'], name='lodges_lodg_created_79d6ea_idx'),
        ),
        migrations.AddIndex(
            model_name='room',
            index=models.Index(fields=['type', '-created_at', 'price'], name='lodges_room_type_f5e1ff_idx'),
        ),
    ]
