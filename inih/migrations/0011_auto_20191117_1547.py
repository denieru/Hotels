# Generated by Django 2.2.7 on 2019-11-17 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inih', '0010_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inih',
            name='author',
        ),
        migrations.RemoveField(
            model_name='servh',
            name='author',
        ),
    ]