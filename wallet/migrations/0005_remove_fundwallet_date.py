# Generated by Django 5.0.6 on 2024-06-28 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_fundwallet_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundwallet',
            name='date',
        ),
    ]
