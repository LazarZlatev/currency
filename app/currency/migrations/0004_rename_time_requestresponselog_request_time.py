# Generated by Django 4.2.7 on 2023-12-16 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_requestresponselog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestresponselog',
            old_name='time',
            new_name='request_time',
        ),
    ]
