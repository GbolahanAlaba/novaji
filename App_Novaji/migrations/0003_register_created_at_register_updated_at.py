# Generated by Django 5.1.1 on 2024-10-24 10:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Novaji', '0002_rename_mobile_number_register_mobile_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='register',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
