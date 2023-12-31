# Generated by Django 4.2 on 2023-11-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0007_lodge_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lodge',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='lodge',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
