# Generated by Django 4.2 on 2023-12-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_useraccount_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
