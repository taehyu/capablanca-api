# Generated by Django 3.0.5 on 2020-06-11 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200611_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='guest',
        ),
    ]
