# Generated by Django 4.2 on 2023-12-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_useraccount_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(default='img.jpg', upload_to='avatar/'),
        ),
    ]