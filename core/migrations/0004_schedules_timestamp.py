# Generated by Django 5.1.6 on 2025-03-11 01:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_schedules_activities'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
