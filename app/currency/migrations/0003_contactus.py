# Generated by Django 4.2.7 on 2023-11-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=254)),
                ('message', models.CharField(max_length=254)),
            ],
        ),
    ]