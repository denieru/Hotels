# Generated by Django 2.2.7 on 2019-11-14 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inih', '0005_auto_20191114_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='fecha_cm',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='menu',
            name='fecha_pm',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
