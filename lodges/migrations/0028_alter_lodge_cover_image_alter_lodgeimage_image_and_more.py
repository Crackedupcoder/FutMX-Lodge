# Generated by Django 4.2 on 2024-01-06 15:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0027_alter_lodge_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodge',
            name='cover_image',
            field=models.ImageField(default='11756.jpg', upload_to='lodge/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='lodgeimage',
            name='image',
            field=models.ImageField(upload_to='lodges/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='cover_image',
            field=models.ImageField(default='11756.jpg', upload_to='rooms/'),
        ),
        migrations.AlterField(
            model_name='roomimage',
            name='image',
            field=models.ImageField(upload_to='rooms/'),
        ),
    ]
