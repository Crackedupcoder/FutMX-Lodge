# Generated by Django 4.2 on 2024-01-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0023_lodge_lodges_lodg_created_79d6ea_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodge',
            name='cover_image',
            field=models.ImageField(default='11756.jpg', upload_to='lodge/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='cover_image',
            field=models.ImageField(default='11756.jpg', upload_to='rooms/'),
        ),
    ]