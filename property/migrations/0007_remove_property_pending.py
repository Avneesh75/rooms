# Generated by Django 3.2.15 on 2023-06-21 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_property_pending'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='pending',
        ),
    ]