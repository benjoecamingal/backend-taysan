# Generated by Django 5.1.6 on 2025-03-15 14:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_healthinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthinfo',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_health_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='healthinfo',
            name='created_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_info', to=settings.AUTH_USER_MODEL),
        ),
    ]
