# Generated by Django 2.2.7 on 2019-11-17 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('inih', '0009_auto_20191116_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('karma', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
