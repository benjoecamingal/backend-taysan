# Generated by Django 5.1.6 on 2025-03-12 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_schedules_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='medical_role',
            field=models.CharField(blank=True, choices=[('nurse', 'Nurse'), ('encoder', 'Encoder'), ('citizen', 'Citizen')], max_length=225, null=True),
        ),
    ]
