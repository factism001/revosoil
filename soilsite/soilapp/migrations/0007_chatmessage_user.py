# Generated by Django 4.2.5 on 2023-10-13 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soilapp', '0006_soildata_delete_soilproperty'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
