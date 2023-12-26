# Generated by Django 4.2 on 2023-12-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0012_alter_room_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]